# 
#=============
# = Settings =
#============================================================

# If you only want this to work on a single network
networkName = ''

#============================================================
import znc

class serverNotice(znc.Module):
    description = "Sends wallops, & locops to Mod"  
    module_types = [znc.CModInfo.UserModule] 

    def OnRaw(self, line):
        try:
            if networkName != '' and self.GetNetwork() != networkName: return znc.CONTINUE 
            ircmsg = str(line)
            if ((' WALLOPS :' not in ircmsg) 
              and (' LOCOPS :' not in ircmsg)
              ): return znc.CONTINUE
            if ircmsg.startswith('@'): ircmsg = ircmsg.split(' ',1)[1]
            msgSplit = ircmsg.split(' ',2)
            fullFrom = msgSplit[0]
            fromName = fullFrom.split('!',1)[0][1:]
            cmd = msgSplit[1]
            message = msgSplit[2]
            if message.startswith(':'): message = message[1:]
            if cmd != 'WALLOPS' and cmd != 'LOCOPS' : return znc.CONTINUE 
            msg = f'{fromName} {cmd.lower()}: {message}'  
            self.sendToMod(msg)
            return znc.HALT
        except:
            return znc.CONTINUE 
            
