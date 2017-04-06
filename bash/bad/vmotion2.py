from vmware import VmwareLib
from pyVmomi import vim

def vmotion(si, vm_name, esx_host, datastore,obj):
	# Finding source VM
	vm = obj.get_vm_by_name(si, vm_name)
	# Finding source Host
	esx_host = obj.get_host_by_name(si, esx_host)

	datastore = obj.get_datastore_by_name(si, datastore)
	print datastore

	if(vm and esx_host):
		# relocate spec, to migrate to another host
		# this can do other things, like storage and resource pool
		# migrations
		relocate_spec = vim.vm.RelocateSpec(host=esx_host, datastore=datastore)
		print relocate_spec
		try:
			# does the actual migration to host
			print vm.RelocateVM_Task(relocate_spec)
			print "Vm Migrated Successfully"
		except:
			print "Vm Migration is Not Successful , Something went wrong"


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
    host_name = "192.168.50.17"
    datastore = "host-17-DS-1"
    vmotion(si, vm_name, host_name,datastore, obj)

    # Disconnecting to Vcenter
    obj.disconnect(si)