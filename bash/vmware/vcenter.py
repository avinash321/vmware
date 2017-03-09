from pyVim.connect import SmartConnect, Disconnect
import ssl

def connect():
	s = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
	s.verify_mode = ssl.CERT_NONE
	global c
	try:
	    c = SmartConnect(host="183.82.41.58", user="root", pwd='Nexii@123')
	    print('Valid certificate')
	except:
	    c = SmartConnect(host="183.82.41.58", user="root", pwd='Nexii@123', sslContext=s)
	    print "successfully connected"

def disConnect(): 
	Disconnect(c)
	print "successfully disconnected"

def currentDate():
	print "Current Date time"
	print(c.CurrentTime())

def vsphere_info():
	vinfo = c.content.about
	print vinfo

def datacenters():
	print "List of Data Centers:"
	datacenter = c.content.rootFolder.childEntity
	for i in datacenter:
   		print i.name

def vmlist():
	print "List of Vm's in the Data Center:"
	datacenter = c.content.rootFolder.childEntity[1]
	vms = datacenter.vmFolder.childEntity
	for i in vms:
		print i.name

def datastores():
	print "List of data stores:"
	datacenter = c.content.rootFolder.childEntity[1]

def vm_PowerON():
	print "VM Power ON"
	datacenter = c.content.rootFolder.childEntity[1]
	vm=datacenter.vmFolder.childEntity[4]
	val=vm.PowerOnVM_Task()
	print val

def vm_PowerOFF():
	print "VM Power ON"
	datacenter = c.content.rootFolder.childEntity[1]
	vm=datacenter.vmFolder.childEntity[4]
	val=vm.PowerOFFVM_Task()
	print val

if __name__ == "__main__":
	connect()
	currentDate()
	vsphere_info()
	datacenters()
	vmlist()
	disConnect()



