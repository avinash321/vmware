from pyVmomi import vim
from pyVim.connect import SmartConnect, Disconnect
import time
import ssl

class VmwareLib:
        
    def connect(self, vcenter_ip, username, password):
        try:
            si = SmartConnect(host = vcenter_ip, user = username, pwd = password)
            return si

        except ssl.SSLError:
            s = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
            s.verify_mode = ssl.CERT_NONE
            print "Trying to Connect Vcenter ......"
            try:
                si = SmartConnect(host = vcenter_ip, user = username, pwd = password, sslContext = s)
                if si:
                    print "Connected to Vcenter Successfully"
                    return si
            except Exception as err:
                print err.msg
                return None
        except Exception as err:
            print "Something went wrong"
            return None

    def disconnect(self,si):
        #print "Trying to Disconnect Vcenter ......"
        try:   
            Disconnect(si)
            print "Disconeected to Vcenter Successfully"
        except Exception as err:
            print err.message

    def reboot_host(self,host,force):
        try:
            t = host.RebootHost_Task(force)
            status = t.info.state
            if status == "success":
                print "Rebooted the Host successfully"
                return 0
            elif status == "running":
                print "Rebooted the Host is in progress"
                return -1
            elif status == "error":
                print "failed to Rebooted the Host"
                return -1
        except Exception as err:
            print err.message
            print "Failed to Reboot, something went wrong"
            return None

    def shut_down_host(self,host):
        try:
            #TODO return value should be handled
            t = host.ShutdownHost_Task(True)
            status = t.info.state
            if status == "success":
                print "ShutdownHost the Host successfully"
                return 0
            elif status == "running":
                print "ShutdownHost the Host is in progress"
                return -1
            elif status == "error":
                print "failed to ShutdownHost the Host"
                return -1
        except Exception as err:
            print err.message
            print "Failed to ShutdownHost, something went wrong"
            return None


    def enter_maintanence_mode(self, host, timeout):
        try:
            t = host.EnterMaintenanceMode_Task(timeout)
            status = t.info.state
            time.sleep(20)
            if status == "success":
                print "Enter maintanence mode successfully"
                return 0
            elif status == "running":
                print "Enter maintanence is in progress"
                return -1
            elif status == "error":
                print "failed to Enter maintanence mode"
                return -1
        except Exception as err:
            print err.message
            print "Failed to put into maintanencemode, something went wrong"
            return None

    def exit_maintanence_mode(self, host, timeout):
        try:
            t = host.ExitMaintenanceMode_Task(timeout)
            status = t.info.state
            time.sleep(15)
            if status == "success":
                print "Exit maintanence mode successfully"
                return 0
            elif status == "running":
                print "Exit maintanence mode is in progress"
                return -1
            elif status == "error":
                print "failed to Exit maintanence mode"
                return -1

        except Exception as err:
            print err.message
            print "Failed to put into exit maintanencemode, something went wrong"
            return None

    def get_obj(self,content, vimtype, name):
        obj = None
        container = content.viewManager.CreateContainerView(content.rootFolder, vimtype, True)
        for c in container.view:
            if c.name == name:
                obj = c
                break
        return obj

    def get_vm_by_name(self, si, name):
        vm = self.get_obj(si.RetrieveContent(), [vim.VirtualMachine], name)
        if vm:
            return vm
        else:
            print "There is no vm , with the given name: "+ name
            return None

    def get_host_by_name(self,si, name):
        host = self.get_obj(si.RetrieveContent(), [vim.HostSystem], name) 
        if host:
            return host
        else:
            print "There is no host , with the given name: "+ name    
            return None

    def get_datacenter_by_name(self,si,name):
        datacenter = self.get_obj(si.RetrieveContent(), [vim.Datacenter],name)
        if datacenter:
            return datacenter
        else:
            print "There is no datacenter , with the given name: "+ name
            return None

    def get_datastore_by_name(self,si,name):
        datastore = self.get_obj(si.RetrieveContent(), [vim.Datastore],name)
        if datastore:
            return datastore
        else:
            print "There is no datastore , with the given name: "+ name   
            return None  

    def disk_space_of_vm(self,vm):
        return_value = None
        for device in vm.config.hardware.device:
            if type(device).__name__ == 'vim.vm.device.VirtualDisk':
                #print 'SIZE', device.deviceInfo.summary
                return_value = device.capacityInKB
        return return_value

    def get_vmdk(self, vm):
        for device in vm.config.hardware.device:
            if type(device).__name__ == 'vim.vm.device.VirtualDisk':
                return device.backing.fileName

    def disk_space_increase(self,si,vmdk,datacenter,sizeinkb,eagerzero):
        try:
            virtualDiskManager = si.content.virtualDiskManager
            task = virtualDiskManager.ExtendVirtualDisk(vmdk ,datacenter,sizeinkb,eagerzero)
            while task.info.state not in [vim.TaskInfo.State.success, vim.TaskInfo.State.error]:
                time.sleep(1)
        except Exception as err:
            print err.message
            print "Unable to increase the increase the disk space, somethin went"

    def power_off_vm(self,vm):
        try:
            power = self.power_state_vm(vm)
            if power == "poweredOff":
                print "The given Vm is allready powered Off"
                return power
            else:
                power = vm.PowerOffVM_Task()
                time.sleep(10)
                status = power.info.state
                if status == "success":
                    print "The given Vm "+ vm.name.upper() +", Powered Off Successfully"
                    return power
                elif status == "running":
                    print "The given Vm "+ vm.name.upper() +", trying to power off"
                    return power
                elif status == "error":
                    print "The given Vm "+ vm.name.upper() +", Failed to power off"
                    return power
        except Exception as err:

            print "something went wrong, unable to power off the VM"
            print err.message
            return None

    def power_on_vm(self,vm):
        try:
            power = self.power_state_vm(vm)
            if power == "poweredOn":
                print "The given Vm is allready powered on"
                return power
            else:
                power = vm.PowerOnVM_Task()
                time.sleep(10)
                status = power.info.state
                if status == "success":
                    print "The given Vm "+ vm.name.upper() +", Powered ON Successfully"
                    return power
                elif status == "running":
                    print "The given Vm "+ vm.name.upper() +", trying to power ON"
                    return power
                elif status == "error":
                    print "The given Vm "+ vm.name.upper() +", Failed to power ON"
                    return power
        except Exception as err:
            print "something went wrong, unable to power on the VM"
            print err.message
            return None

    def power_state_vm(self,vm):
        try:
            power = vm.runtime.powerState
            print "The given Vm "+ vm.name.upper() + " Power Status is: " + '\033[1m' + power.upper() + '\033[0m'
            return power
        except Exception as err:
            print "something went wrong, unable to print the power state of the VM"
            print err.message
            return None



if __name__ == "__main__":

    vcenter_ip = "183.82.41.58"
    username = "root"
    password = "VMware@123"

    # Creating Object for VMware Class
    obj = VmwareLib(vcenter_ip, username, password)

    # Connecting to Vcenter
    si = obj.connect()

    #Getting the Required VM Object name by it's ID
    vm = obj.get_vm_by_name(si,"avinash")
    print vm.name

    obj.power_state_vm(vm)


    # Disconnecting to Vcenter
    obj.disconnect(si)
