from pyVmomi import vim
from pyVim.connect import SmartConnect, Disconnect
import time
import ssl
import logging

logging.basicConfig(filename="log_general.txt",level=logging.DEBUG,
format = "%(asctime)s-->%(levelname)s-->%(message)s")
class Akward():
    def __init__(self):
        self.si =None

    def connect(self, vcenter_ip, username, password):
        '''Vcenter connection:
        This is to create Vcenter server Instance. This will make the connection to the given 
        vcenter server ip by verifying the given username and password and returns that connection object'''
        try:
            si = SmartConnect(host = vcenter_ip, user = username, pwd = password)
            logging.info("Connected to Vcenter Successfully")
            self.si = si
            return si

        except ssl.SSLError:
            s = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
            s.verify_mode = ssl.CERT_NONE
            logging.info("Trying to Connect Vcenter ......")
            try:
                si = SmartConnect(host = vcenter_ip, user = username, pwd = password, sslContext = s)
                if si:
                    logging.info("Connected to Vcenter Successfully")
                    self.si = si
                    return si
            except Exception as err:
                return None
        except Exception as err:
            logging.info("Something went wrong (please check your Vcenter Ip)")
            return None

    def disconnect(self):
        '''Disconnecting Vcenter
        This is to Ddestroy Vcenter server Instance. 
        This will disconnects the vcenter'''
        try:
            Disconnect(self.si)
            logging.info("Disconeected to Vcenter Successfully")
        except Exception as err:
            logging.info(err.message)

    def get_obj(self,content, vimtype, name):
        '''getobject: this will returns the concerned vimtype object'''
        obj = None
        container = content.viewManager.CreateContainerView(content.rootFolder, vimtype, True)
        for c in container.view:
            if c.name == name:
                obj = c
                break
        return obj
    def get_host_by_name(self, name):
        '''gethost by name: this will returns the host object based on the given host name'''
        host = self.__get_obj(self.si.RetrieveContent(), [vim.HostSystem], name) 
        if host:
            return host
        else:
            logging.info("There is no host , with the given name: "+ name)   
            return None

    def get_datastore_by_name(self,name):
        '''getdatastore by name: this will returns the datastore object based on the given datastore name'''
        datastore = self.__get_obj(self.si.RetrieveContent(), [vim.Datastore],name)
        if datastore:
            return datastore
        else:
            logging.info("There is no datastore , with the given name: "+ name)
            return None 

    def get_vm_by_name(self, name):
        '''getvm by name: this will returns the vm object based on the given vm name'''
        vm = self.__get_obj(self.si.RetrieveContent(), [vim.VirtualMachine], name)
        if vm:
            return vm
        else:
            logging.info("There is no vm , with the given name: "+ name)
            return None

    def get_pool_by_name(self, name):
        '''getvm by name: this will returns the vm object based on the given vm name'''
        vm = self.__get_obj(self.si.RetrieveContent(), [vim.ResourcePool], name)
        if vm:
            return vm
        else:
            logging.info("There is no vm , with the given name: "+ name)
            return None


if __name__ == "__main__":
    vcenter_ip = "183.82.41.58"
    username = "root"
    password = "Nexii@123"

    
    obj = Akward()
    # connection
    si  = obj.connect(vcenter_ip, username, password)
    

    # Disconnection
    obj.disconnect()


    