#!/usr/bin/python
from pyVmomi import vim
from pyVim import connect
import ssl
import vmutils

def get_vim_objects(content, vim_type):
	'''Get vim objects of a given type.'''
	return [item for item in content.viewManager.CreateContainerView(
	content.rootFolder, [vim_type], recursive=True).view]

si=vmutils.connect()
content = si.RetrieveContent()


#Templates List
for vm in get_vim_objects(content, vim.VirtualMachine):
	if vm.config.template: 
		print "Template Name : ", vm.name