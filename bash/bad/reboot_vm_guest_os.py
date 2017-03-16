from pyVmomi import vim
from pyVim.connect import SmartConnect, Disconnect
import getpass
import vmutils
import ssl


si = vmutils.connect()

vm_name = raw_input('VM: ')
# Finding source VM
vm = vmutils.get_vm_by_name(si, vm_name)

def shutdown_guest(vm):
	vm.ShutdownGuest()
	print "Guest OS Shutdown Successfully"


def reset_guest_info(vm):
	vm.ResetGuestInformation()
	print "Resetting the Guest Information Successful"


def standby_guest():
	vm.StandbyGuest(vm)
	print "Standby Guest successful"

def reboot_guest(vm):
	# does the actual vm reboot
	try:
	    vm.RebootGuest()
	    print "Guest OS Rebooted Successfully"
	except:
	    # forceably shutoff/on
	    # need to do if vmware guestadditions isn't running
	    vm.ResetVM_Task()
	    print "Failed to Reboot the Guest OS"

if __name__ == "__main__":
	reboot_guest(vm)

	#Disconnect to Vcenter
	vmutils.disconnect(si)