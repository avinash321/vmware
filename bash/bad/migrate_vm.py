from pyVmomi import vim
import vmutils
import random

si = vmutils.connect()

vm_name = raw_input('test2')
esx_host = raw_input('192.168.50.14')

if esx_host == '':
    all_hosts = vmutils.get_hosts(si)
    esx_host = vmutils.get_host_by_name(si, random.choice(all_hosts.values()))
else:
	esx_host = vmutils.get_host_by_name(si, esx_host)

# Finding source VM
vm = vmutils.get_vm_by_name(si, vm_name)

# relocate spec, to migrate to another host
# this can do other things, like storage and resource pool
# migrations
relocate_spec = vim.vm.RelocateSpec(host=esx_host)

# does the actual migration to host
print vm.Relocate(relocate_spec)

#print "Vm Migrated Successfully"

vmutils.disconnect(si)