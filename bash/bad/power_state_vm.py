from pyVmomi import vim
import vmutils

# Connect to Vcenter
si=vmutils.connect()

# Finding source VM , that need to  Power Off
vm_name = raw_input("Enter the VM name, that you want to know the  Power Status: ")
vm = vmutils.get_vm_by_name(si, vm_name)
#power_state=vim.vm.PowerState
power_state=vm.runtime.powerState
print power_state
print "The given Vm "+ vm.name.upper() + "Power Status is: " + power_state

vmutils.disconnect(si)