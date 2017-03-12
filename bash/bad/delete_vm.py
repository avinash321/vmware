from pyVmomi import vim
import vmutils

# Connect to Vcenter
si=vmutils.connect()

# Finding source VM , that need to  Power Off
vm_name = raw_input("Enter the VM name, that you want to power off: ")
vm = vmutils.get_vm_by_name(si, vm_name)

# We need to power off the Vm , before deletion
vm.PowerOffVM_Task()
print "The given Vm "+ vm.name.upper() +", Powered Off Successfully"

# Deletion of VM
vm.Destroy_Task()
print "The given Vm "+ vm.name.upper() +", Deleted Successfully"

vmutils.disconnect(si)