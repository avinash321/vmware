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


datastore=datacenter.datastore[0]
print datastore

#VM Folder
vmfolder=datacenter.vmFolder

print vmfolder
print vmfolder.name

vmlist=vmfolder.childEntity
global vm
for i in vmlist:
	if i.name=="python":
		vm=i
		break

print "avinash "+ vm.name

# First Parameter
template1=vm

# set relospec
relospec = vim.vm.RelocateSpec()
relospec.datastore = datastore
#relospec.pool = resource_pool



clonespec = vim.vm.CloneSpec()
clonespec.location = relospec
clonespec.powerOn = True
clonespec.template = False

print "cloning VM..."
template1.Clone(folder=vmfolder, name="avinash30", spec=clonespec)

print "successful"



# Location




#print vim.vm.ConfigIvmnfo()





















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