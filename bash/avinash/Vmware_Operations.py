from pyVmomi import vim, vmodl
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

    def reboot_host(self,host_ip):
        '''Reboot Esxi host:
        It will reboot the given esxi host.
        Parameters: ip of the host, thst you want to reboot'''
        host = self.__get_host_by_name(host_ip)
        force=True
        if host:
            try:
                task = host.RebootHost_Task(force)
                while task.info.state not in [vim.TaskInfo.State.success, vim.TaskInfo.State.error]:
                    time.sleep(1)
                status = task.info.state
                if status == "success":
                    logging.info("Rebooted the host successfully")
                if status == "error":
                    logging.info("errr: Unable to reboot the host")
                return status
            except Exception as err:
                logging.info(err.message)
                logging.info("Exception: Failed to Reboot the host, something went wrong")
                return None
        else:
            logging.info("Unable to perform the Reboot host")                


    def shutdown_host(self,host_ip):
        '''Shutdown Esxi host:
        It will reboot the given esxi host.
        Parameters: ip of the host, thst you want to reboot'''
        host = self.__get_host_by_name(host_ip)
        force=True
        if host:
            try:
                task = host.ShutdownHost_Task(force)
                while task.info.state not in [vim.TaskInfo.State.success, vim.TaskInfo.State.error]:
                    time.sleep(1)
                status = task.info.state
                if status == "success":
                    logging.info("Rebooted the host successfully")
                if status == "error":
                    logging.info("errr: Unable to reboot the host")
                return status
            except Exception as err:
                logging.info("Exception': Failed to ShutdownHost, something went wrong")
                logging.info(err.message)
                return None
        else:
            logging.info("Unable to perform the Shutdown host")

    def enter_maintanence_mode(self, host_name, timeout):
        '''Enter Maintanence mode:
        this will put the the esxi host into maintanence mode
        This will takes the parameters , hostname and expected time to complete the operation'''
        host = self.__get_host_by_name(host_name)
        if host:
            try:
                task = host.EnterMaintenanceMode_Task(timeout)
                logging.info(task.info.state)
                while task.info.state not in [vim.TaskInfo.State.success, vim.TaskInfo.State.error]:
                    time.sleep(1)
                return task.info.state
            except Exception as err:
                logging.info(err.message)
                logging.info("Failed to put into maintanencemode, something went wrong")
                return None
        else:
            logging.info("Unable to perform the enter maintanence mode")

    def exit_maintanence_mode(self, host_name, timeout):
        '''Exit Maintanence mode:
        this will getback the the esxi host from maintanence mode
        This will takes the parameters , hostname and expected time to complete the operation'''
        host = self.__get_host_by_name(host_name)
        if host:
            try:
                task = host.ExitMaintenanceMode_Task(timeout)
                logging.info(task.info.state)
                while task.info.state not in [vim.TaskInfo.State.success, vim.TaskInfo.State.error]:
                    time.sleep(1)
                return task.info.state
            except Exception as err:
                logging.info(err.message)
                logging.info("Failed to put into exit maintanencemode, something went wrong")
                return None
        else:
            logging.info("Unable to perform the Exit maintanence mode")

    def disk_space_increase(self, vm_name, new_size, datacenter_name):
        '''Thsi will increses the diskspace of the given vm.
        While performing this operation , Vm will be powered off automatically if it is on and then verifies ,
        the newly given disk space with initial diskspace.
        The new disk space shuld be greater than the initial diskspace'''
        power_status = self.power_state_vm(vm_name)
        if power_status == "poweredOn":
            logging.info("powering of the vm...")
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
                    logging.info("Disk space increased succesfully")
                    # disk space of the VM After increasing
                    logging.info("New Disk space is : "+ str(new_diskspace/ (1024*1024)) + "GB")
                    return new_diskspace/ (1024*1024)
                else:
                    logging.info("Disk space Not increased")
                    return -1
            else:
                raise VMNoDatacenterFound("Datacenter Not Found Error")
        else:
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
            logging.info(err.message)
            logging.info("Unable to increase the increase the disk space, somethin went wrong")

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
            logging.info("There is no datacenter , with the given name: "+ name)
            return None

    def __get_host_by_name(self, name):
        '''gethost by name: this will returns the host object based on the given host name'''
        host = self.__get_obj(self.si.RetrieveContent(), [vim.HostSystem], name) 
        if host:
            return host
        else:
            logging.info("There is no host , with the given name: "+ name)   
            return None

    def __get_pool_by_name(self, name):
        '''getvm by name: this will returns the vm object based on the given vm name'''
        pool = self.__get_obj(self.si.RetrieveContent(), [vim.ResourcePool], name)
        if pool:
            return pool
        else:
            logging.info("There is no pool , with the given name: "+ name)
            return None

    def __get_datastore_by_name(self,name):
        '''getdatastore by name: this will returns the datastore object based on the given datastore name'''
        datastore = self.__get_obj(self.si.RetrieveContent(), [vim.Datastore],name)
        if datastore:
            return datastore
        else:
            logging.info("There is no datastore , with the given name: "+ name)
            return None 

    def __get_vm_by_name(self, name):
        '''getvm by name: this will returns the vm object based on the given vm name'''
        vm = self.__get_obj(self.si.RetrieveContent(), [vim.VirtualMachine], name)
        if vm:
            return vm
        else:
            logging.info("There is no vm , with the given name: "+ name)
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
                disk_space = device.capacityInKB
        return disk_space

    def power_off_vm(self,vm_name):
        '''Power Off VM:
        This will power off the vm based on the given vm name'''
        vm = self.__get_vm_by_name(vm_name)
        try:
            power = self.power_state_vm(vm_name)
            if power == "poweredOff":
                logging.info("The given Vm is allready powered Off")
                return power
            else:
                logging.info("The given Vm is Powered ON")
                logging.info("Trying to power off the VM....")
                task = vm.PowerOffVM_Task()
                while task.info.state not in [vim.TaskInfo.State.success, vim.TaskInfo.State.error]:
                    time.sleep(1)
                status = task.info.state
                if status == "success":
                    logging.info("The given Vm "+ vm.name.upper() +", Powered Off Successfully")
                    return status
                elif status == "error":
                    logging.info("The given Vm "+ vm.name.upper() +", Failed to power off")
                    return status      
        except Exception as err:
            logging.info("something went wrong, unable to power off the VM")
            logging.info(err.messag)
            return None

    def power_on_vm(self,vm_name):
        '''Power ON VM:
        This will power on the vm based on the given vm name'''
        vm = self.__get_vm_by_name(vm_name)
        try:
            logging.info("Checking the power status of the VM")
            power = self.power_state_vm(vm_name)
            if power == "poweredOn":
                logging.info("The given Vm is allready powered ON")
                return power
            else:
                task = vm.PowerOnVM_Task()
                while task.info.state not in [vim.TaskInfo.State.success, vim.TaskInfo.State.error]:
                    time.sleep(1)
                status = task.info.state
                if status == "success":
                    logging.info("The given Vm "+ vm.name.upper() +", Powered ON Successfully")
                    return status
                elif status == "error":
                    logging.info("The given Vm "+ vm.name.upper() +", Failed to power ON")
                    return status
        except Exception as err:
            logging.info("something went wrong, unable to power on the VM")
            logging.info(err.message)
            return None

    def power_state_vm(self,vm_name):
        '''Power State of VM:
        This will power status based on the given vm name'''
        vm = self.__get_vm_by_name(vm_name)
        try:
            power = vm.runtime.powerState
            logging.info("The given Vm "+ vm.name.upper() + " Power Status is: " + power.upper())
            return power
        except Exception as err:
            logging.info("something went wrong, unable to display the power state of the VM")
            logging.info(err.message)
            return None

    def migration(self,vm_name, esx_host, pool):
        '''This method will performs the host migration.The vm should be powerd off while migrating.
        And this willl performs Host vmotion only.In vmware documentation , the resource pool parameter is,
        optional, but without resource pool , this functionality ill not work.
        We need to send the paramaters as targetted host
        parameters:  
        vm_name: Name of the Vm that you want to migrate
        esx_host: The Destination (or) Targeted Host, 
        pool : The Destination pool (or) Targeted pool
        '''
        # Finding source VM based on the name
        vm = self.__get_vm_by_name(vm_name)
        # Finding Targeted Host (or) Destination Host based on the host ip
        host = self.__get_host_by_name(esx_host)
        # Importent * finding resource pool based on the pool name
        # Here we need to give the ****destination pool******
        pool = self.__get_pool_by_name(pool)

        migrate_priority = vim.VirtualMachine.MovePriority.defaultPriority

        # Powering off the Vm 
        if(vm and host and pool):
            # relocate spec, to migrate to another host
            # this can do other things, like storage migration
            try:
                task = vm.Migrate(pool = pool, host = host, priority = migrate_priority)
                while task.info.state not in [vim.TaskInfo.State.success, vim.TaskInfo.State.error]:
                    time.sleep(1)
                status = task.info.state
                if status == "success":
                    logging.info("The given Vm "+ vm.name.upper() +", Migrated Successfully")
                    return status
                elif status == "error":
                    logging.info("The given Vm "+ vm.name.upper() +", Failed to Migrate")
                    return status 

            except vmodl.MethodFault, e:
                print "Caught vmodl fault: %s" % e.msg
            except Exception, e:
                print "Caught exception: %s" % str(e)
                print e.message

        elif(vm == None):
            logging.info("The given vm not found")
        elif(host == None):
            logging.info("The given Host not found")
        elif(pool == None):
            logging.info("The given pool not found")

if __name__ == '__main__':
    obj = Vmware_Operations()
    obj.connect("183.82.41.58", "root","Nexii@123")
    obj.migration("fancy", "192.168.50.16",'pool-16')
    #obj.disk_space_increase("avinash", 9, "Nexiilabs")