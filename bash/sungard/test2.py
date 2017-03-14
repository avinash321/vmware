from pyVim.connect import SmartConnect, Disconnect
import ssl
from pyVmomi import vim
import all
import time

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
host = all.get_host_by_name(c,"192.168.50.17")
print host.name
k=host.network
print k
n=None
for i in k:
	if (i.name == 'Network11'):
		n=i
print n
print n.name
n.Destroy_Task()
time.sleep(5)
n.DestroyNetwork()
print "Network Destroyed Successfully"

	



#--------------------------------------------------------------------------------------------
Disconnect(c)
print "successfully disconnected"
