from pyVmomi import vim
from pyVim.connect import SmartConnect, Disconnect
import vmutils
import random

si = None
username = raw_input('root')
password = raw_input('Nexii@123')
vcenter = raw_input('183.82.41.58')
vm_name = raw_input('test2')
esx_host = raw_input('192.168.50.14')

try:
    si = SmartConnect(host=vcenter, user=username, pwd=password, port=443)
except IOError, e:
    pass

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
vm.Relocate(relocate_spec)

Disconnect(si)