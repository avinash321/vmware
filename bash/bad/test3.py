from pyVmomi import vim
import vmutils
import time

# Connect to Vcenter
si=vmutils.connect()

# Finding source VM , to create a template of it
vm_name = raw_input("Enter the VM name, that you want to mark as tmplate: ")
vm = vmutils.get_vm_by_name(si, vm_name)

# We need to power off the Vm before marking as template
vm.MarkAsVirtualMachine()

print "The given Vm "+ vm.name.upper() +", Powered Off Successfully"

print "Please wait ...."
time.sleep(6)
resource_pool = None



vm.MarkAsTemplate(resource_pool)
print "The given Vm "+ vm_name.upper() +" marked as tmplate Successfully"

vmutils.disconnect(si)