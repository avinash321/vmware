from pyVmomi import vim
import connect
import time

# Connect to Vcenter
si=connect.connect()

# Finding source VM , to create a template of it
vm_name = raw_input("Enter the VM name, that you want to mark as tmplate: ")
vm = connect.get_vm_by_name(si, vm_name)

# We need to power off the Vm before marking as template
vm.PowerOffVM_Task()
print "The given Vm "+ vm.name.upper() +", Powered Off Successfully"

print "Please wait ...."
time.sleep(6)

vm.MarkAsVirtualMachine()
print "The given Vm "+ vm_name.upper() +" marked as Virtual machine Successfully"

connect.disconnect(si)