'''
This will connects the Vcenter and 
Disconnects the Vcenetr

'''
from vmware import VmwareLib

# Creating the object for vmwareLib class
def name(vm_name, obj):

	vm = obj.get_vm_by_name(si,vm_name)
	print vm

if __name__ == "__main__":

    # Creating Object for VMwareLib Class
    obj = VmwareLib()

    vcenter_ip = "183.82.41.58"
    username = "root"
    password = "VMware@123"

    # Connecting to Vcenter
    si = obj.connect(vcenter_ip, username, password)

    #vm operation
    name("avinash", obj)

    # Disconnecting to Vcenter
    obj.disconnect(si)

