from pyVmomi import vim
from pyVim.connect import SmartConnect, Disconnect
import vmutils
import ssl

s = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
s.verify_mode = ssl.CERT_NONE
c = None
try:
    c = SmartConnect(host="183.82.41.58", user="root", pwd='Nexii@123')
    print('Valid certificate')
except:
    c = SmartConnect(host="183.82.41.58", user="root", pwd='Nexii@123', sslContext=s)
    print "successfully connected"

# Finding source VM
template_vm = vmutils.get_vm_by_name(si, 'centos-6.5-x64')

Disconnect(c)
print "successfully disconnected"