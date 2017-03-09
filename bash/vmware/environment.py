from pyVim.connect import SmartConnect, Disconnect
import ssl
from pyVmomi import vim

s = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
s.verify_mode = ssl.CERT_NONE
global c
try:
    c = SmartConnect(host="183.82.41.58", user="root", pwd='Nexii@123')
    print('Valid certificate')
except:
    c = SmartConnect(host="183.82.41.58", user="root", pwd='Nexii@123', sslContext=s)
    print "successfully connected" 


# Vcenter
content=c.content
rootfolder=content.rootFolder

#DataCenter
datacenters=rootfolder.childEntity
datacenter=datacenters[1]

#VM Folder
vmfolder=datacenter.vmFolder
vmlist=vmfolder.childEntity

# VM
vm=vmlist[2]

print vm.name

# Reboot
#vm.RebootGuest()
#vm.Reload()
#vm.PowerOffVM_Task()
#vm.PowerOnVM_Task()


Disconnect(c)
print "successfully disconnected"