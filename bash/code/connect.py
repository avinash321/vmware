'''
This will connects the Vcenter and 
Disconnects the Vcenetr

'''
from vmware import VmwareLib

# Creating the object for vmwareLib class
obj = VmwareLib()

# Connecting to Vcenter Server
si = obj.connect()
vm_name = raw_input("Enter the Vm name: ")
vm = obj.get_vm_by_name(si,vm_name)

k = obj.disk_space_of_vm(vm)
print k

print type(k)

# Disconnecting form Vcenetr
obj.disconnect(si)

