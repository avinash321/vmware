import vmutils
import yaml

si = vmutils.connect()

# Finding source VM , that need to  Power Off
vm_name = raw_input("Enter the VM name, that you want to increase the Disk space: ")
new_vm = vmutils.get_vm_by_name(si, vm_name)

# Increasing the disk space code
for dev in new_vm.config.hardware.device:
    if hasattr(dev.backing, 'abc.yml'):
        if dev.deviceInfo.label in vm_disk.keys():
            capacity_in_kb = dev.capacityInKB
            new_disk_kb = int(vm_disk[dev.deviceInfo.label]['size_gb']) * 1024 * 512
            if new_disk_kb > capacity_in_kb:
                dev_changes = []
                disk_spec = vim.vm.device.VirtualDeviceSpec()
                disk_spec.operation = vim.vm.device.VirtualDeviceSpec.Operation.edit
                disk_spec.device = vim.vm.device.VirtualDisk()
                disk_spec.device.key = dev.key
                disk_spec.device.backing = vim.vm.device.VirtualDisk.FlatVer2BackingInfo()
                disk_spec.device.backing.fileName = dev.backing.fileName
                disk_spec.device.backing.diskMode = dev.backing.diskMode
                disk_spec.device.controllerKey = dev.controllerKey
                disk_spec.device.unitNumber = dev.unitNumber
                disk_spec.device.capacityInKB = new_disk_kb
                dev_changes.append(disk_spec)

                spec = vim.vm.ConfigSpec()
                spec.deviceChange = dev_changes

                task = new_vm.ReconfigVM_Task(spec=spec)

vmutils.disconnect(si)