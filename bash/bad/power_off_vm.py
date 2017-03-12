from pyVmomi import vim
import vmutils

# Connect to Vcenter
si=vmutils.connect()

# Finding source VM , that need to  Power Off
vm_name = raw_input("Enter the VM name, that you want to power off: ")
vm = vmutils.get_vm_by_name(si, vm_name)

vm.PowerOffVM_Task()
print "The given Vm "+ vm.name.upper() +", Powered Off Successfully"

vmutils.disconnect(si)