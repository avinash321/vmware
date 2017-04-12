'''
 Connect to the Linux VM
########################################
Linux Machine IP: 192.168.50.18
Username: root
Password: Nexii@123

'''
import sys, traceback, paramiko, logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ConnLinuxCls(object):
    def __init__(self):
        #self.conn = self.connectLinux()
        pass
    
    def connectLinux(self):
        try:
            self.client = paramiko.SSHClient()
            self.client.load_system_host_keys()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            logger.info( "Connecting to Linux VM...")
            self.port = 22
            self.client.connect(self.host_ip, self.port, self.u_name, self.pwd)
            return self.client 
        except Exception, e:
            logger.info( "Exception : {}".format(e))
            traceback.print_exc()
            try:
                self.client.close()
            except:
                pass
            sys.exit(1)
    def executeCommand(self):
        #Testing exec_command
        '''
        stdin, stdout, stderr  = self.conn.exec_command("ifconfig")
        logger.info( "The output : {}".format(stdout.readlines()))
        '''
        # Scan the LUNs 
        stdin, stdout, stderr  = self.conn.exec_command("# echo '---' > /sys/class/fc_host/host0/issue_lip")
        logger.info( "The output : {}".format(stdout.readlines()))