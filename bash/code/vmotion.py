from vmware import VmwareLib
from pyVmomi import vim

def vmotion(vm, host):
	vm_name = vm
	esx_host = host

	# Finding source VM
	vm = obj.get_vm_by_name(si, vm_name)

	# Finding source Host
	esx_host = obj.get_host_by_name(si, esx_host)

	# relocate spec, to migrate to another host
	# this can do other things, like storage and resource pool
	# migrations
	relocate_spec = vim.vm.RelocateSpec(host=esx_host)

	# does the actual migration to host
	print vm.Relocate(relocate_spec)

	#print "Vm Migrated Successfully"


if __name__ == "__main__":

    # Creating Object for VMwareLib Class
    obj = VmwareLib()

    vcenter_ip = "183.82.41.58"
    username = "root"
    password = "VMware@123"

    # Connecting to Vcenter
    si = obj.connect(vcenter_ip, username, password)

    #Vmotion operation
    vm_name = "avinash"
    host_name = "192.168.50.16"
    vmotion(vm_name, host_name)

    # Disconnecting to Vcenter
    obj.disconnect(si)