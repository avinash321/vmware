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

#------------------------------------------------------------------------------------------
content = c.RetrieveContent()
vm = get_obj(content, [vim.VirtualMachine], args.vm_name)
#--------------------------------------------------------------------------------------------
Disconnect(c)
print "successfully disconnected"
