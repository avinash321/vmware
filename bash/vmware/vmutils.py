from pyVim.connect import SmartConnect, Disconnect
import ssl
from pyVmomi import vim

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


def get_vm_by_name(name):

	# Vcenter
	content=c.content
	rootfolder=content.rootFolder

	#DataCenter
	datacenters=rootfolder.childEntity
	datacenter=datacenters[1]

	#VM Folder
	vmfolder=datacenter.vmFolder
	vmlist=vmfolder.childEntity
	vm = None
	for i in vmlist:
		if i.name==name:
			vm=i
			print "The given Vm "+ name + " is available"
			break
	if vm == None:
		print"The given vm "+ name + " Was not Found"




def avinash():
	obj=c.content.viewManager
	print obj

def _get_all_objs():
    """
    Get all the vsphere objects associated with a given type
    """
    content=c.content
    vimtype=content.rootFolder.childEntity[1].vmFolder.childEntity
    obj = {}
    container = content.viewManager.CreateContainerView(content.rootFolder, vimtype, True)
    for k in container.view:
        obj.update({k: k.name})
	return obj

def disconnect():
	Disconnect(c)
	print "successfully disconnected"

def get_vm(c,name):
	#Find a virtual machine by it's name and return it
    return get_obj(c.RetrieveContent(), vimtype, name)

def get_all_objs(content, vimtype):
	obj = {}
	container = content.viewManager.CreateContainerView(content.rootFolder, vimtype, True)
	for c in container.view:
		obj.update({c: c.name})
		for i in obj:
			print i
	return obj


def get_obj(content, vimtype, name):
	obj = None
	container = content.viewManager.CreateContainerView(content.rootFolder, vimtype, True)
	for c in container.view:
		if c.name == name:
			obj = c
			print obj
			print "The given machine was found successfully"
			break	
	return obj      

def get_resoursepool(content, vimtype):
	obj=None
	container = content.viewManager.CreateContainerView(content.rootFolder, vimtype, True)
	for c in container.view:
		print c

if __name__ == "__main__":
	connect()
	#get_vm_by_name("python")
	#get_vm(c,"python")

	# get_all_objs(c.RetrieveContent(), [vim.VirtualMachine])
	# get_all_objs(c.RetrieveContent(), [vim.Datastore])
	# get_all_objs(c.RetrieveContent(), [vim.ResourcePool])
	# get_all_objs(c.RetrieveContent(), [vim.HostSystem])
	#get_obj(c.RetrieveContent(),[vim.VirtualMachine],"controller")
	get_resoursepool(c.RetrieveContent(),[vim.ResourcePool])
	



	
	disconnect()
