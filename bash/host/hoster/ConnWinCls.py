'''
Connect to the Windows VM
##############################
Windows Machine IP: 192.168.50.13
Username: administrator
Password: Nexii@123
Install pywinrm on Windows machine

'''
from winrm.protocol import Protocol
import logging 

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ConnWinCls(object):
    def __init__(self):
        self.conn = self.connectWindows()

    def connectWindows(self):
        try:
            self.hostIP = "https://"+self.host_ip + ":5986/wsman"
            self.pro = Protocol(
                endpoint = self.hostIP,
                transport = "ntlm",
                username = self.u_name,
                password = self.pwd,
                server_cert_validation ="ignore")
            logger.info("Connecting Windows ...")
            script = """diskpart /s C:\Users\Administrator\Desktop\script1.txt > C:\Users\Administrator\Desktop\log1.txt"""
            shell_id = self.pro.open_shell()
            logger.info("Connected")
            command_id = self.pro.run_command(shell_id, script)

            std_out, std_err, status_code = self.pro.get_command_output(shell_id, command_id)
            logger.info("Executed Cmd status_code is : {}".format(status_code))
            logger.info("Executed Command Output is : {}".format(std_out))
            logger.info("Executed Command Error is : {}".format(std_err))
            self.pro.cleanup_command(shell_id, command_id)
            self.pro.close_shell(shell_id)
        except Exception, e:
            logger.info( "Exception : {}".format(e))
            



