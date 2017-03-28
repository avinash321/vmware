from pyVmomi import vim
import vmutils


# Connect to Vcenter
si=vmutils.connect()

# Finding source VM , that need to  Power Off
vm_name = raw_input("Enter the VM name: ")
vm = vmutils.get_vm_by_name(si, vm_name)
spec = vm.config
print spec
print "success"


vmutils.disconnect(si)