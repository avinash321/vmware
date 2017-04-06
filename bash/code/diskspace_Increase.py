'''
this will Increse the Disk space of he VM
'''
from vmware import VmwareLib
import time

class VMNoDatacenterFound(Exception):
    pass
class VmNotFoundException(Exception):
    pass

def get_vm(si, vm_name, obj):
    vm = obj.get_vm_by_name(si,vm_name)
    return vm

def power_off_vm(vm,obj):
    status = obj.power_state_vm(vm)
    if status == "poweredOn":
        print "powering off the Vm......."
        status = obj.power_off_vm(vm)
    else:
        print "something went wrong"
        return status

def initial_diskspace(vm,obj):
    # disk space of the VM Before increasing
    try:
        initial_diskspace = obj.disk_space_of_vm(vm)
        return initial_diskspace
    except Exception as err:
        err.message
        return None

# Here the value represents in gb
def increase_disk(vm, obj, new_size, initial_diskspace,datacenter_name):
    if new_size > initial_diskspace:
        # Getting Vmdk for the given vm
        vmdk = obj.get_vmdk(vm)
        eagerzero = False
        datacenter = obj.get_datacenter_by_name(si,datacenter_name)

        if datacenter:
            # This will increase the disk space
            task = obj.disk_space_increase(si,vmdk,datacenter,new_size,eagerzero)
            # Verifying weather disk sapce is is increaswed or not
            new_diskspace = obj.disk_space_of_vm(vm)
            if new_diskspace > initial_diskspace:
                print "Disk space increased succesfully"
                # disk space of the VM After increasing
                print "New Disk space is : "+ str(new_diskspace/ (1024*1024)) + "GB"
                return new_diskspace/ (1024*1024)
                return 0
            else:
                print "Disk space Not increased"
                return -1
        else:
            raise VMNoDatacenterFound("Datacenter Not Found Error")
    else:
        print "The Initial capacity is :" + str(initial_diskspace/ (1024*1024) )+ "GB"
        print "The Given New capacity is: " + str(new_size/ (1024*1024))+ "GB"
        
        print "Newsize should be greater than Initial size"
        return -1


if __name__ == "__main__":

    vcenter_ip = "183.82.41.58"
    username = "root"
    password = "Nexii@123"

    # Creating Object for VMware Class
    obj = VmwareLib()


    # Connecting to Vcenter
    si = obj.connect(vcenter_ip, username, password)
    if si:
        #Disk Increasing Operation
        #step1: (Getting the Target VM)
        vm_name = "avinash"
        vm = get_vm(si, vm_name, obj)

        if vm:
            #Step2: Checking the powersgtatus of the VM , If power is ON , it will Power off the VM
            power_off_vm(vm, obj)
            #Step3: checking the initial disk space
            initial_diskspace = initial_diskspace(vm, obj)
            print "The actual capacity of the disk is :" + str(initial_diskspace/(1024*1024))
            new_size = input("Enter the new capacity in GB: ")
            new_size = new_size * (1024 * 1024)
            datacenter_name = "Nexiilabs"
            increase_disk(vm, obj, new_size, initial_diskspace, datacenter_name)
            # Disconnecting to Vcenter
        else:
            raise VmNotFoundException("Vm Not Found Error")
        obj.disconnect(si)


