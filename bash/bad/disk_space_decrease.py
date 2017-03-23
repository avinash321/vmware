from pyVmomi import vim
import vmutils
import time


si = vmutils.connect()
content1=si.content
rootfolder=content1.rootFolder

#DataCenter
datacenters=rootfolder.childEntity
datacenter=datacenters[1]


virtualDiskManager = si.content.virtualDiskManager
task = virtualDiskManager.ShrinkVirtualDisk_Task("[datastore1 (1)] python/python.vmdk" ,datacenter,False)


while task.info.state not in [vim.TaskInfo.State.success, vim.TaskInfo.State.error]:
	time.sleep(1)

print "Disk space increased succesfully"

vmutils.disconnect(si)