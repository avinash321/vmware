from pyVmomi import vim
import vmutils
import time

def inflate(datacenter):
    print "trying to inflate"
    task1 = virtualDiskManager.InflateVirtualDisk_Task("[datastore1 (1)] avinash/avinash.vmdkk",datacenter)
    while task1.info.state not in [vim.TaskInfo.State.success, vim.TaskInfo.State.error]:
        time.sleep(1)
    print  task1.info.state

def shrink(datacenter):
    print "trying to shrinking"
    task2 = virtualDiskManager.ShrinkVirtualDisk_Task("[datastore1 (1)] avinash/avinash.vmdk" ,datacenter,False)
    while task2.info.state not in [vim.TaskInfo.State.success, vim.TaskInfo.State.error]:
        time.sleep(1)
    print  task2.info.state
    
if __name__ == "__main__":

    si = vmutils.connect()
    content1=si.content
    rootfolder=content1.rootFolder

    #DataCenter
    datacenters=rootfolder.childEntity
    datacenter=datacenters[1]


    virtualDiskManager = si.content.virtualDiskManager
    inflate(datacenter)
    shrink(datacenter)
    vmutils.disconnect(si)