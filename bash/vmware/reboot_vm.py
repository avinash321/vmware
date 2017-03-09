from pyVmomi import vim
from pyVim.connect import SmartConnect, Disconnect
import getpass
import vmutils
import ssl


username = "root"
password = "Nexii@123"
vcenter = "183.82.41.58"
vm_name = "ubuntu16.04"

s = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
s.verify_mode = ssl.CERT_NONE
global c
try:
    c = SmartConnect(host=vcenter, user=username, pwd=password)
    print('Valid certificate')
except:
    c = SmartConnect(host=vcenter, user=username, pwd=password, sslContext=s)
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
global vm
for i in vmlist:
	if i.name == "ubuntu16.04":
		vm=i
		break
print vm
#print vm.name
# does the actual vm reboot

print "reboot test"
try:
    vm.RebootGuest()
    print "Successfully Rebooted"

except:
    # forceably shutoff/on
    # need to do if vmware guest additions isn't running
    vm.ResetVM_Task()
    print "Unable to reboot Now"

Disconnect(c)
print "Disconnected successflly"