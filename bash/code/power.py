from vmware import VmwareLib

# Creating the object for vmwareLib class
obj = VmwareLib()

# Connecting to Vcenter Server
si = obj.connect()

vm_name = raw_input("Enter the Vm name: ")
vm = obj.get_vm_by_name(si,vm_name)

# Power on VM 
print "plese select any one of the follwing options"
n = input("1.Power ON VM    2.Power OFF VM    3.Power state of VM:  ")

if n==1:
	obj.power_on_vm(vm)

elif n==2:
	obj.power_off_vm(vm)

elif n==3:
	obj.power_state_vm(vm)

else:
	print "please select valid option"

# Disconnecting form Vcenetr
obj.disconnect(si)