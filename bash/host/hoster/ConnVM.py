"""
Library for connecting and executing commands on windows and Linux machines
"""

from ConnWinCls import ConnWinCls
from ConnLinuxCls import ConnLinuxCls
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ConnVMCls(ConnWinCls, ConnLinuxCls):
    """
    Common class for Connecting Windows and Linux machines
    """
    def __init__(self, vm_type, host_ip, u_name, pwd):
        """
        Init method
        """
        self.vm_type = vm_type
        self.host_ip = host_ip
        self.u_name = u_name
        self.pwd = pwd
       
        ConnLinuxCls.__init__(self) # for Linux
       

if __name__ == "__main__":

    vm_type = raw_input("Enter Windows or Linux : ")
    host_ip = raw_input("Enter host IP : ")
    u_name = raw_input("Enter the user name : ")
    pwd = raw_input("Enter the password : ")

    cvcObj = ConnVMCls(vm_type,host_ip,u_name,pwd)
    
    if (cvcObj.vm_type.lower() == "windows"):
        CONN = cvcObj.connectWindows()
    elif (cvcObj.vm_type.lower() == "linux"):
        CONN = cvcObj.connectLinux()
        logger.info( cvcObj.executeCommand())
    else:
        logger.info( "Invalid Option")

     #NFS client Machine
    '''
    cvcObj = ConnLinuxCls(vm_type,host_ip,u_name,pwd)
    cvcObj.connectLinux()
    cvcObj.executeCommand('ifconfig')

    #NFS Server Machine
    cvcServerObj = ConnLinuxCls(vm_type,host_ip,u_name,pwd)
    cvcServerObj.connectLinux()
    
    # Installing and Starting the services on both server and client machines
    # place a 'if' condition to check is it already installed
    cvcObj.executeCommand('yum install nfs-utils nfs-utils-lib')
    cvcObj.executeCommand('/etc/init.d/portmap start')
    cvcObj.executeCommand('/etc/init.d/nfs start')
    cvcObj.executeCommand('chkconfig --level 35 portmap on')
    cvcObj.executeCommand('chkconfig --level 35 nfs on')
    
    cvcServerObj.executeCommand('yum install nfs-utils nfs-utils-lib')
    cvcServerObj.executeCommand('/etc/init.d/portmap start')
    cvcServerObj.executeCommand('/etc/init.d/nfs start')
    cvcServerObj.executeCommand('chkconfig --level 35 portmap on')
    cvcServerObj.executeCommand('chkconfig --level 35 nfs on')

    #Setting up the NFS server
    #Creating a new director nfsshare1
    cvcServerObj.executeCommand('mkdir /nfsshare1')
    cmd2 = """vi /etc/exports /nfsshare """+ host_ip +"""(rw,sync,no_root_squash)"""
    cvcServerObj.executeCommand(cmd2)

    #Setting up the NFS client
    #Mount shared NFS directory
    cvcObj.executeCommand('mount -t nfs 192.168.0.100:/nfsshare /mnt/nfsshare')

'''
