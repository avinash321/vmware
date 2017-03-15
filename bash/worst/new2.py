def clone_vm(
content, template, vm_name, si, ip,
datacenter_name, vm_folder, datastore_name,
cluster_name, resource_pool, power_on):
"""
Clone a VM from a template/VM, datacenter_name, vm_folder, datastore_name
cluster_name, resource_pool, and power_on are all optional.
"""

# if none git the first one
datacenter = get_obj(content, [vim.Datacenter], datacenter_name)

if vm_folder:
    destfolder = get_obj(content, [vim.Folder], vm_folder)
else:
    destfolder = datacenter.vmFolder

if datastore_name:
    datastore = get_obj(content, [vim.Datastore], datastore_name)
else:
    datastore = get_obj(
        content, [vim.Datastore], template.datastore[0].info.name)

# if None, get the first one
cluster = get_obj(content, [vim.ClusterComputeResource], cluster_name)

if resource_pool:
    resource_pool = get_obj(content, [vim.ResourcePool], resource_pool)
else:
    resource_pool = cluster.resourcePool

# set relospec
relospec = vim.vm.RelocateSpec()
relospec.datastore = datastore
relospec.pool = resource_pool

deviceToChange = None
for device in template.config.hardware.device:
        if isinstance(device, vim.vm.device.VirtualEthernetCard):
            deviceToChange = device


#guest NIC settings
nic = vim.vm.device.VirtualDeviceSpec()
nic.operation = vim.vm.device.VirtualDeviceSpec.Operation.edit  # or add to make a new one
nic.device = deviceToChange
nic.device.wakeOnLanEnabled = True
nic.device.addressType = 'assigned'   #mac address assigned by virtual center
nic.device.key = 4000  # 4000 seems to be the value to use for a vmxnet3 device
# nic.device.deviceInfo = vim.Description()
# nic.device.deviceInfo.label = "Network Adapter"
# nic.device.deviceInfo.summary = "summary text here"


#"adapter map"  no idea wtf this is
guest_map = vim.vm.customization.AdapterMapping()
guest_map.adapter = vim.vm.customization.IPSettings()
guest_map.adapter.ip = vim.vm.customization.FixedIp()
guest_map.adapter.ip.ipAddress = str(ip)
guest_map.adapter.subnetMask = str(subnet)
guest_map.adapter.gateway = str(gateway)

# DNS settings
globalip = vim.vm.customization.GlobalIPSettings()
globalip.dnsServerList = dns
# globalip.dnsSuffixList = ip_settings[0]['domain']         #do I need this? I don't think so

# Hostname settings
ident = vim.vm.customization.Sysprep()
ident.guiUnattended = vim.vm.customization.GuiUnattended()
ident.guiUnattended.autoLogon = False #the machine does not auto-logon
ident.guiUnattended.password  = vim.vm.customization.Password()
ident.guiUnattended.password.value = vm_password
ident.guiUnattended.password.plainText = True  #the password passed over is not encrypted 
ident.userData = vim.vm.customization.UserData()
ident.userData.fullName = "Derek Chadwell"
ident.userData.orgName = "NetApp"
ident.userData.computerName = vim.vm.customization.FixedName()
ident.userData.computerName.name = vm_name
ident.identification = vim.vm.customization.Identification()


# create spec to change host IP address
customspec = vim.vm.customization.Specification()
customspec.nicSettingMap = [guest_map]
customspec.globalIPSettings = globalip
customspec.identity = ident

# VM config spec
vmconf = vim.vm.ConfigSpec()
#vmconf.numCPUs = deploy_settings['cpus']
#vmconf.memoryMB = deploy_settings['mem']
#vmconf.cpuHotAddEnabled = True
#vmconf.memoryHotAddEnabled = True
vmconf.deviceChange = [nic]


clonespec = vim.vm.CloneSpec()
clonespec.location = relospec
clonespec.config = vmconf
clonespec.customization = customspec
clonespec.powerOn = power_on
clonespec.template = False

print "cloning VM..."
task = template.Clone(folder=destfolder, name=vm_name, spec=clonespec)
wait_for_task(task)