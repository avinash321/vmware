from pyVmomi import vim
from pyVim.connect import SmartConnect, Disconnect
import ssl

def connect():
	s = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
	s.verify_mode = ssl.CERT_NONE
	global si
	try:
	    si = SmartConnect(host="183.82.41.58", user="root", pwd='Nexii@123')
	    print('Valid certificate')
	except:
	    si = SmartConnect(host="183.82.41.58", user="root", pwd='Nexii@123', sslContext=s)
	    print "successfully connected"

def disConnect(): 
	Disconnect(si)
	print "successfully disconnected"

def clone_vm():

# Finding source VM
	newvm = "python_vm_clone"
	# Vcenter
	content=si.content
	rootfolder=content.rootFolder

	#DataCenter
	datacenters=rootfolder.childEntity
	datacenter=datacenters[1]

	#VM Folder
	vmfolder=datacenter.vmFolder
	vmlist=vmfolder.childEntity
	global vm
	for i in vmlist:
		if i.name=="python":
			vm=i
			break
	template_vm =vm

	'''
	There are two roads for modifying a vm creation from a template
	1. ConfigSpec -> CloneSpec
	2. ConfigSpec -> (AdapterMapping -> GlobalIPSettings -> LinuxPrep) -> CustomSpec -> CloneSpec
	Notes: 
	    ConfigSpec and CustomSpecificiation are purely optional and
	    independent
	'''

	# cpu/ram changes
	#mem = 512 * 1024 # convert to GB
	mem = 50  # MB
	vmconf = vim.vm.ConfigSpec(numCPUs=1, memoryMB=mem)
	#vmconf.deviceChange = devices

	# Network adapter settings
	adaptermap = vim.vm.customization.AdapterMapping()
	adaptermap.adapter = vim.vm.customization.IPSettings(ip=vim.vm.customization.DhcpIpGenerator(), dnsDomain='domain.local')
	# static ip
	#adaptermap.adapter = vim.vm.customization.IPSettings(ip=vim.vm.customization.FixedIp(address='10.0.1.10'),
	#                                                     subnetMask='255.255.255.0', gateway='10.0.0.1')

	# IP
	globalip = vim.vm.customization.GlobalIPSettings()
	# for static ip
	#globalip = vim.vm.customization.GlobalIPSettings(dnsServerList=['10.0.1.4', '10.0.1.1'])

	# Hostname settings
	ident = vim.vm.customization.LinuxPrep(domain='domain.local', hostName=vim.vm.customization.FixedName(name=newvm))

	# Putting all these pieces together in a custom spec
	customspec = vim.vm.customization.Specification(nicSettingMap=[adaptermap], globalIPSettings=globalip, identity=ident)


	# Creating relocate spec and clone spec
	resource_pool = vmutils.get_resource_pool(si, 'DEV')
	relocateSpec = vim.vm.RelocateSpec(pool=resource_pool)
	#cloneSpec = vim.vm.CloneSpec(powerOn=True, template=False, location=relocateSpec, customization=customspec, config=vmconf)
	cloneSpec = vim.vm.CloneSpec(powerOn=True, template=False, location=relocateSpec, customization=None, config=vmconf)

	# Creating clone task
	clone = template_vm.Clone(name=newvm, folder=template_vm.parent, spec=cloneSpec)


if __name__=="__main__":
	connect()
	clone_vm()
	disConnect()