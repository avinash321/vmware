from pyVmomi import vim
import vmutils

# Connect to Vcenter
si=vmutils.connect()

# Finding source VM , to create a template of it
vm_name = raw_input("Enter the VM name, that you want to mark as tmplate: ")
vm = vmutils.get_vm_by_name(si, vm_name)

# We need to power off the Vm before marking as template
vm.PowerOffVM_Task()
print "The given Vm "+ vm.name.upper() +", Powered Off Successfully"


vm.MarkAsTemplate()
print "The given Vm "+ vm.name.upper() +" marked as tmplate Successfully"

vmutils.disconnect(si)

