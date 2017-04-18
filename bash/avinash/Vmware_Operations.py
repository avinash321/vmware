from pyVmomi import vim
from pyVim.connect import SmartConnect, Disconnect
import time
import ssl
import logging

logging.basicConfig(filename="log_general.txt",level=logging.DEBUG,
format = "%(asctime)s-->%(levelname)s-->%(message)s")

class Vmware_Operations():
    def __init__(self):
        self.si =None

    def connect(self, vcenter_ip, username, password):
        '''Vcenter connection:
        This is to create Vcenter server Instance. This will make the connection to the given 
        vcenter server ip by verifying the given username and password and returns that connection object'''
        try:
            si = SmartConnect(host = vcenter_ip, user = username, pwd = password)
            self.si = si
            return si

        except ssl.SSLError:
            s = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
            s.verify_mode = ssl.CERT_NONE
            print "Trying to Connect Vcenter ......"
            try:
                si = SmartConnect(host = vcenter_ip, user = username, pwd = password, sslContext = s)
                if si:
                    print "Connected to Vcenter Successfully"
                    self.si = si
                    return si
            except Exception as err:
                return None
        except Exception as err:
            print "Something went wrong (please check your Vcenter Ip)"
            return None

    def disconnect(self):
        '''Disconnecting Vcenter
        This is to Ddestroy Vcenter server Instance. 
        This will disconnects the vcenter'''
        try:
            Disconnect(self.si)
            print "Disconeected to Vcenter Successfully"
        except Exception as err:
            print err.message

    def reboot_host(self,host_ip):
        '''Reboot Esxi host:
        It will reboot the given esxi host.
        Parameters: ip of the host, thst you want to reboot'''
        host = self.__get_host_by_name(host_ip)
        force=True
        try:
            task = host.RebootHost_Task(force)
            while task.info.state not in [vim.TaskInfo.State.success, vim.TaskInfo.State.error]:
                time.sleep(1)
            status = task.info.state
            if status == "success":
                print "Rebooted the host successfully"
            if status == "error":
                print "errr: Unable to reboot the host"
            return status
        except Exception as err:
            print err.message
            print "Exception: Failed to Reboot the host, something went wrong"
            return None

    def shutdown_host(self,host_ip):
        '''Shutdown Esxi host:
        It will reboot the given esxi host.
        Parameters: ip of the host, thst you want to reboot'''
        host = self.__get_host_by_name(host_ip)
        force=True
        try:
            task = host.ShutdownHost_Task(force)
            while task.info.state not in [vim.TaskInfo.State.success, vim.TaskInfo.State.error]:
                time.sleep(1)
            status = task.info.state
            if status == "success":
                print "Rebooted the host successfully"
            if status == "error":
                print "errr: Unable to reboot the host"
            return status
        except Exception as err:
            print "Exception': Failed to ShutdownHost, something went wrong"
            print err.message
            return None

    def enter_maintanence_mode(self, host_name, timeout):
        '''Enter Maintanence mode:
        this will put the the esxi host into maintanence mode
        This will takes the parameters , hostname and expected time to complete the operation'''
        host = self.__get_host_by_name(host_name)
        try:
            task = host.EnterMaintenanceMode_Task(timeout)
            print task.info.state
            while task.info.state not in [vim.TaskInfo.State.success, vim.TaskInfo.State.error]:
                time.sleep(1)
            return task.info.state
        except Exception as err:
            print err.message
            print "Failed to put into maintanencemode, something went wrong"
            return None

    def exit_maintanence_mode(self, host_name, timeout):
        '''Exit Maintanence mode:
        this will getback the the esxi host from maintanence mode
        This will takes the parameters , hostname and expected time to complete the operation'''
        host = self.__get_host_by_name(host_name)
        try:
            task = host.ExitMaintenanceMode_Task(timeout)
            print task.info.state
            while task.info.state not in [vim.TaskInfo.State.success, vim.TaskInfo.State.error]:
                time.sleep(1)
            return task.info.state
        except Exception as err:
            print err.message
            print "Failed to put into exit maintanencemode, something went wrong"
            return None

    def disk_space_increase(self, vm_name, new_size, datacenter_name):
        '''Thsi will increses the diskspace of the given vm.
        While performing this operation , Vm will be powered off automatically if it is on and then verifies ,
        the newly given disk space with initial diskspace.
        The new disk space shuld be greater than the initial diskspace'''
        power_status = self.power_state_vm(vm_name)
        if power_status == "poweredOn":
            print "powering of the vm..."
            self.power_off_vm(vm_name)
        initial_diskspace = self.__get_disk_space_of_vm(vm_name)
        new_size = int(new_size) * (1024*1024)
        if new_size > initial_diskspace:
            # Getting Vmdk for the given vm
            vmdk = self.__get_vmdk(vm_name)
            eagerzero = False
            datacenter = self.__get_datacenter_by_name(datacenter_name)
            if datacenter:
                # This will increase the disk space
                task = self.__increase_disk(vmdk,datacenter,new_size,eagerzero)
                time.sleep(15)
                # Verifying weather disk sapce is is increaswed or not
                new_diskspace = self.__get_disk_space_of_vm(vm_name)
                if new_diskspace > initial_diskspace:
                    print "Disk space increased succesfully"
                    logging.info("Disk space increased succesfully")
                    # disk space of the VM After increasing
                    print "New Disk space is : "+ str(new_diskspace/ (1024*1024)) + "GB"
                    logging.info("New Disk space is : "+ str(new_diskspace/ (1024*1024)) + "GB")
                    return new_diskspace/ (1024*1024)
                else:
                    print "Disk space Not increased"
                    logging.info("Disk space Not increased")
                    return -1
            else:
                raise VMNoDatacenterFound("Datacenter Not Found Error")
        else:
            print "The Initial capacity is :" + str(initial_diskspace/ (1024*1024) )+ "GB"
            print "The Given New capacity is: " + str(new_size/ (1024*1024))+ "GB"
            print "Newsize should be greater than Initial size"
            logging.info("The Initial capacity is :" + str(initial_diskspace/ (1024*1024) )+ "GB")
            logging.info("The Given New capacity is: " + str(new_size/ (1024*1024))+ "GB")
            logging.info("Newsize should be greater than Initial size")
            return -1

    def __increase_disk(self,vmdk,datacenter,sizeinkb,eagerzero):
        try:
            virtualDiskManager = self.si.content.virtualDiskManager
            task = virtualDiskManager.ExtendVirtualDisk(vmdk ,datacenter,sizeinkb,eagerzero)
            while task.info.state not in [vim.TaskInfo.State.success, vim.TaskInfo.State.error]:
                time.sleep(1)
            return task.info.state
        except Exception as err:
            print err.message
            print "Unable to increase the increase the disk space, somethin went wrong"

    def __get_obj(self,content, vimtype, name):
        '''getobject: this will returns the concerned vimtype object'''
        obj = None
        container = content.viewManager.CreateContainerView(content.rootFolder, vimtype, True)
        for c in container.view:
            if c.name == name:
                obj = c
                break
        return obj

    def __get_datacenter_by_name(self,name):
        '''getdatacenter by name: this will returns the Datacenter object based on the given datacenter name'''
        datacenter = self.__get_obj(self.si.RetrieveContent(), [vim.Datacenter],name)
        if datacenter:
            return datacenter
        else:
            print "There is no datacenter , with the given name: "+ name
            return None

    def __get_host_by_name(self, name):
        '''gethost by name: this will returns the host object based on the given host name'''
        host = self.__get_obj(self.si.RetrieveContent(), [vim.HostSystem], name) 
        if host:
            return host
        else:
            print "There is no host , with the given name: "+ name    
            return None

    def __get_datastore_by_name(self,name):
        '''getdatastore by name: this will returns the datastore object based on the given datastore name'''
        datastore = self.__get_obj(self.si.RetrieveContent(), [vim.Datastore],name)
        if datastore:
            return datastore
        else:
            print "There is no datastore , with the given name: "+ name   
            return None 

    def __get_vm_by_name(self, name):
        '''getvm by name: this will returns the vm object based on the given vm name'''
        vm = self.__get_obj(self.si.RetrieveContent(), [vim.VirtualMachine], name)
        if vm:
            return vm
        else:
            print "There is no vm , with the given name: "+ name
            return None

    def __get_vmdk(self, vm_name):
        '''getVMDK:
        this will returns the virtual machine disk file based on the given vm name'''
        vm = self.__get_vm_by_name(vm_name)
        return_value = None
        for device in vm.config.hardware.device:
            if type(device).__name__ == 'vim.vm.device.VirtualDisk':
                vmdk_path = device.backing.fileName
        return vmdk_path
 
    def __get_disk_space_of_vm(self,vm_name):
        '''Disk space of the vm:
        it will returns the diskspace of the vm in kb'''
        vm = self.__get_vm_by_name(vm_name)
        return_value = None
        for device in vm.config.hardware.device:
            if type(device).__name__ == 'vim.vm.device.VirtualDisk':
                #print 'SIZE', device.deviceInfo.summary
                disk_space = device.capacityInKB
        return disk_space

    def power_off_vm(self,vm_name):
        '''Power Off VM:
        This will power off the vm based on the given vm name'''
        vm = self.__get_vm_by_name(vm_name)
        print vm.name
        try:
            power = self.power_state_vm(vm_name)
            print "chck vm"
            if power == "poweredOff":
                print "The given Vm is allready powered Off"
                return power
            else:
                task = vm.PowerOffVM_Task()
                print "poweroff"
                while task.info.state not in [vim.TaskInfo.State.success, vim.TaskInfo.State.error]:
                    time.sleep(1)
                status = task.info.state
                if status == "success":
                    print "The given Vm "+ vm.name.upper() +", Powered Off Successfully"
                    return status
                elif status == "error":
                    print "The given Vm "+ vm.name.upper() +", Failed to power off"
                    return status      
        except Exception as err:
            print "something went wrong, unable to power off the VM"
            print err.message
            return None

    def power_on_vm(self,vm_name):
        '''Power ON VM:
        This will power on the vm based on the given vm name'''
        vm = self.__get_vm_by_name(vm_name)
        try:
            power = self.power_state_vm(vm_name)
            if power == "poweredOn":
                print "The given Vm is allready powered on"
                return power
            else:
                task = vm.PowerOnVM_Task()
                while task.info.state not in [vim.TaskInfo.State.success, vim.TaskInfo.State.error]:
                    time.sleep(1)
                status = task.info.state
                if status == "success":
                    print "The given Vm "+ vm.name.upper() +", Powered ON Successfully"
                    return status
                elif status == "error":
                    print "The given Vm "+ vm.name.upper() +", Failed to power ON"
                    return status
        except Exception as err:
            print "something went wrong, unable to power on the VM"
            print err.message
            return None

    def power_state_vm(self,vm_name):
        '''Power State of VM:
        This will power status based on the given vm name'''
        vm = self.__get_vm_by_name(vm_name)
        try:
            power = vm.runtime.powerState
            print "The given Vm "+ vm.name.upper() + " Power Status is: " + power.upper()
            logging.info("The given Vm "+ vm.name.upper() + " Power Status is: " + power.upper())
            return power
        except Exception as err:
            print "something went wrong, unable to print the power state of the VM"
            print err.message
            return None



if __name__ == '__main__':
    obj = Vmware_Operations()
    obj.connect("183.82.41.58", "root","Nexii@123")
    obj.disk_space_increase("avinash", 9, "Nexiilabs")