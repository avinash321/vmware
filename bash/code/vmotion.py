from vmware import VmwareLib

# Creating the object for vmwareLib class
obj = VmwareLib()

# Connecting to Vcenter Server
si = obj.connect()

vm_name = raw_input('VM: ')
esx_host = raw_input('ESX Host: ')

if esx_host == '':
	get_host_by_name(self,si,esx_host)

else:
	esx_host = obj.get_host_by_name(si, esx_host)

# Finding source VM
vm = obj.get_vm_by_name(si, vm_name)

# relocate spec, to migrate to another host
# this can do other things, like storage and resource pool
# migrations
relocate_spec = vim.vm.RelocateSpec(host=esx_host)

# does the actual migration to host
print vm.Relocate(relocate_spec)

#print "Vm Migrated Successfully"

obj.disconnect(si)