from vmware import VmwareLib
from pyVmomi import vim
import time
import logging

logging.basicConfig(filename="log_Esxi_maintanence_mode.txt",level=logging.DEBUG,
format = "%(asctime)s-->%(levelname)s-->%(message)s")

class VmotionException(Exception):
	pass

def vmotion(vm, host):
	vm_name = vm
	esx_host = host

	# Finding source VM
	vm = obj.get_vm_by_name(si, vm_name)
	# Finding source Host
	esx_host = obj.get_host_by_name(si, esx_host)

	if(vm and esx_host):
		# relocate spec, to migrate to another host
		# this can do other things, like storage and resource pool
		# migrations
		relocate_spec = vim.vm.RelocateSpec(host=esx_host)
		try:
			# does the actual migration to host
			task = vm.Relocate(relocate_spec)
            while task.info.state not in [vim.TaskInfo.State.success, vim.TaskInfo.State.error]:
                time.sleep(1)
            ststus = task.info.state
			if status == "success":
				print "Vm Migrated Successfully"
				logging.info("Vm Migrated Successfully")
				return status
			elif status == "error":
				print "failed to migrate the VM"
				logging.info("failed to migrate the VM")
				return status

		except Exception as err:
			logging.Exception(err.message)
			#print "Vm Migration is Not Successful , Something went wrong"
			print None
	else:
		raise VmotionException("Vm or Host Not found Erro")

def main():
    # Creating Object for VMwareLib Class
    logging.info("Program Started")
    obj = VmwareLib()
    vcenter_ip = "183.82.41.58"
    username = "root"
    password = "Nexii@123"
    # Connecting to Vcenter
    si = obj.connect(vcenter_ip, username, password)

    if si:
    	logging.info("Object created for VmwareLib")
    	logging.debug(obj)
	    #Vmotion operation
	    vm_name = "avinash"
	    host_name = "192.168.50.17"
	    vmotion(vm_name, host_name)

	    # Disconnecting to Vcenter
	    obj.disconnect(si)
	logging.info("Program Ended")

if __name__ == "__main__":
	main()