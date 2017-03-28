import vmutils

si = vmutils.connect()

# Finding source VM , that need to  Power Off
vm_name = raw_input("Enter the VM name, that you want to know the disk space: ")
vm = vmutils.get_vm_by_name(si, vm_name)

# Getting disk space of the VM
for device in vm.config.hardware.device:
    if type(device).__name__ == 'vim.vm.device.VirtualDisk':
        print 'SIZE', device.deviceInfo.summary

vmutils.disconnect(si)
