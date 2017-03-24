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
task = virtualDiskManager.QueryVirtualDiskUuid("[datastore1 (1)] python/python.vmdk" ,datacenter)
print task

print "Disk space decreased succesfully"

vmutils.disconnect(si)