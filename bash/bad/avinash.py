from pyVmomi import vim
from pyVim.connect import SmartConnect, Disconnect
import time
import ssl

class VmwareLib:

	def __init__(self):
		global vcenter
		global username
		global password
		global si
		vcenter = "183.82.41.58"
		username = "root"
		password = "VMware@123"

	def connect(self):
		s = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
		s.verify_mode = ssl.CERT_NONE
		try:
			si = SmartConnect(host = self.vcenter, user = self.username, pwd = self.password)
			print "Valid certificate"
			return si
		except:
			print "Trying to Connect Vcenter ......"
			si = SmartConnect(host = vcenter, user = username, pwd = password, sslContext = s)
			print "Connected to Vcenter Successfully"
			return si

	def disconnect(self,si):
		print "Trying to Disconnect Vcenter ......"
		Disconnect(si)
		print "Disconeected to Vcenter Successfully"

	def enter_maintanence_mode(host):
		host.EnterMaintenanceMode_Task(3000)
		print "Enter maintanence mode successfully"

	def exit_maintanence_mode(host):
		host.ExitMaintenanceMode_Task(10)
		print "Exit maintanence mode successfully"

	def get_obj(self,content, vimtype, name):
		obj = None
		container = content.viewManager.CreateContainerView(content.rootFolder, vimtype, True)
		for c in container.view:
			if c.name == name:
				obj = c
				break
		return obj

	def get_vm_by_name(self,si, name):
		vm = self.get_obj(si.RetrieveContent(), [vim.VirtualMachine], name)
		return vm

	def get_host_by_name(self,si, name):
		host = self.get_obj(si.RetrieveContent(), [vim.HostSystem], name)
		return host

	def get_datacenter(self,si,name):
		datacenter = self.get_obj(si.RetrieveContent(), [vim.Datacenter],name)
		return datacenter

	def disk_space_of_vm(self,vm):
		for device in vm.config.hardware.device:
			if type(device).__name__ == 'vim.vm.device.VirtualDisk':
				print 'SIZE', device.deviceInfo.summary

	def disk_space_increase(self,vmdk,datacenter,sizeinkb,eagerzero):
		virtualDiskManager = si.content.virtualDiskManager
		task = virtualDiskManager.ExtendVirtualDisk("[datastore1 (1)] python/python.vmdk" ,datacenter,15*1024*1024,False)
		while task.info.state not in [vim.TaskInfo.State.success, vim.TaskInfo.State.error]:
			time.sleep(1)
		print "Disk space increased succesfully"

	def power_off_vm(self,vm):
		vm.PowerOffVM_Task()
		print "The given Vm "+ vm.name.upper() +", Powered Off Successfully"

	def power_on_vm(self,vm):
		vm.PowerOnVM_Task()
		print "The given Vm "+ vm.name.upper() +", Powered ON Successfully"

	def power_state_vm(self,vm):
		power = vm.runtime.powerState
		print "The given Vm "+ vm.name.upper() + " Power Status is: " + '\033[1m' + power.upper() + '\033[0m'

	def reboot_host(self,host):
		host.RebootHost_Task(True)
		print "Rebooted the Host successfully"

	def shut_down_host(self,host):
		host.ShutdownHost_Task(True)
		print "Shutdown the Host successfully"
		
if __name__ == "__main__":

	# Creating Object for VMware Class
	obj = VmwareLib()

	# Connecting to Vcenter
	si = obj.connect()

	#Getting the Required VM Object name by it's ID
	vm = obj.get_vm_by_name(si,"avinash")
	print vm.name

	obj.power_state_vm(vm)


	# Disconnecting to Vcenter
	obj.disconnect(si)