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
global vm
for i in vmlist:
	if i.name=="python":
		vm=i
		break
print vim.vm.ConfigInfo()

# Powered On VM Task
'''
k=vm.PowerOnVM_Task()
print k
print "Vm Powered On Successfully"
'''


# Powered OFF VM task
'''
k=vm.PowerOffVM_Task()
print k
print "Vm Powered Off Successfull
'''

# Reboot
#vm.RebootGuest()
#vm.Reload()

'''
k=vm.MarkAsTemplate()
print k
print "Template Created Successfully"
'''




Disconnect(c)
print "successfully disconnected"