from pyVmomi import vim
import vmutils

# Connect to Vcenter
si=vmutils.connect()

# Finding source VM , that need to  Power Off
vm_name = raw_input("Enter the VM name, that you want know the power status: ")
vm = vmutils.get_vm_by_name(si, vm_name)
if (vm == None):
	print "The givemn vm is not available"
	print "Please make sure the vm name"

else:
	power = vm.runtime.powerState
	print "The given Vm "+ vm.name.upper() + " Power Status is: " + '\033[1m' + power.upper() + '\033[0m'

vmutils.disconnect(si)