from pyVmomi import vim
import vmutils

# Connect to Vcenter
si=vmutils.connect()

# Finding source VM , that need to  Power Off
vm_name = "VMware vCenter Server Appliance"
vm = vmutils.get_vm_by_name(si, vm_name)

print vm.name

#vm.PowerOffVM_Task()
print "The given Vm "+ vm.name.upper() +", Powered Off Successfully"

vmutils.disconnect(si)