'''
this will Increse the Disk space of he VM
'''
from vmware import VmwareLib


# VM
def getvm(vm_name):
    vm_name = raw_input("Enter the Vm name: ")
    vm = obj.get_vm_by_name(si,vm_name)

def power_status(vm):
    status = obj.power_state_vm(vm)
    if status == "poweredon":
        obj.power_off_vm(vm)

def actual_diskspace(vm)
    # disk space of the VM Before increasing
    actual_diskspace = obj.disk_space_of_vm(vm)
    print "Actual Disk space is : "+ str(actual_diskspace / (1024*1024)) +"GB"



# Here the value represents in gb

new_size_gb = input("enetr the new disk space size (gb): ")
new_size_kb = new_size_gb * (1024*1024)

if new_size_kb > actual_diskspace:
    # Getting Vmdk for the given vm
    vmdk = obj.get_vmdk(vm)
    # geting the DataCenter based on name
    datacenter_name = raw_input("enetr the datacenter name: ")
    datacenter = obj.get_datacenter(si,datacenter_name)

    eagerzero = False

    obj.disk_space_increase(si,vmdk,datacenter,new_size_kb,eagerzero)

    new_diskspace = obj.disk_space_of_vm(vm)
    print new_diskspace

    if  new_diskspace > actual_diskspace:
        print "Disk space increased succesfully"
        # disk space of the VM After increasing
        print "New Disk space is : "+ str(new_diskspace/(1024*1024)) + "GB"

    else:
        print "Disk space was Not increased"
else:
    print "Plese give the disk size above the previous size"


# Disconnecting form Vcenetr
obj.disconnect(si)

if __name __ == "__main__":
    # Creating the object for vmwareLib class
    obj = VmwareLib()
    # Connecting to Vcenter Server
    si = obj.connect()

    vm = getvm(vm_name,obj)
    power_status(vm,obj)
    actual_diskspace(vm,obj)


