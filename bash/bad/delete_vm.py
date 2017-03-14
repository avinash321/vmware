from pyVmomi import vim
import vmutils
import time

# Connect to Vcenter
si=vmutils.connect()

# Finding source VM , that need to  Power Off
vm_name = raw_input("Enter the VM name, that you want to power off: ")
vm = vmutils.get_vm_by_name(si, vm_name)

# We need to power off the Vm , before deletion
vm.PowerOffVM_Task()
print "The given Vm "+ vm.name.upper() +", Powered Off Successfully"

print "Please Wait....."
time.sleep(6)
# Deletion of VM
vm.Destroy_Task()
print "The given Vm "+ vm_name + ", Deleted Successfully"

vmutils.disconnect(si)