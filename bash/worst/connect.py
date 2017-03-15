from pyVmomi import vim
from pyVim.connect import SmartConnect, Disconnect
import time
import ssl
def connect():
    vcenter = "183.82.41.58"
    username = "root"
    password = "Nexii@123"

    si = None
    s = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    s.verify_mode = ssl.CERT_NONE

    try:
        si = SmartConnect(host = vcenter, user = username, pwd = password)
        print "Valid certificate"
        return si
    except:
        si = SmartConnect(host = vcenter, user = username, pwd = password, sslContext = s)
        print "Connected to Vcenter Successfully"
        return si 

def disconnect(si):
    Disconnect(si)
    print "Disconeected to Vcenter Successfully"
