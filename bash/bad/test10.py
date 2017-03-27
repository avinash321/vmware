import vmutils

si = vmutils.connect()


def get_vmdk(vm):
	for device in vm.config.hardware.device:
		if type(device).__name__ == 'vim.vm.device.VirtualDisk':
			return device.backing.fileName


vm_name = raw_input("Enter the VM name, that you want to mark as tmplate: ")
vm = vmutils.get_vm_by_name(si, vm_name)
print get_vmdk(vm)

vmutils.disconnect(si)
