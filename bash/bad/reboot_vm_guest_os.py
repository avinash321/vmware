from pyVmomi import vim
from pyVim.connect import SmartConnect, Disconnect
import getpass
import vmutils
import ssl


si = vmutils.connect()

vm_name = raw_input('VM: ')
# Finding source VM
vm = vmutils.get_vm_by_name(si, vm_name)

# does the actual vm reboot
try:
    vm.RebootGuest()
    print "Guest OS Rebooted Successfully"
except:
    # forceably shutoff/on
    # need to do if vmware guestadditions isn't running
    vm.ResetVM_Task()
    print "Failed to Reboot the Guest OS"

vmutils.disconnect(si)