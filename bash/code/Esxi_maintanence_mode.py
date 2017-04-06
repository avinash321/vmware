'''
This will put the given Esxi Host into maintanence mode
'''
from vmware import VmwareLib
class VMMaintenceException(Exception):
   pass

def maintanencemode(si, host_name, obj):
    host = obj.get_host_by_name(si, host_name)
    timeout = 3000
    # 3000 secends
    # This will put the given Esxi host in maintanence mode
    if host:
       obj.enter_maintanence_mode(host, timeout)
    else:
        raise VMMaintenceException("Host error")

if __name__ == "__main__":

    # Creating Object for VMwareLib Class
    obj = VmwareLib()

    vcenter_ip = "183.82.41.58"
    username = "root"
    password = "VMware@123"

    # Connecting to Vcenter
    si = obj.connect(vcenter_ip, username, password)

    #Reboot operation
    host_name = "192.168.50.22"
    try:
        maintanencemode(si, host_name, obj)
    except VMMaintenceException as vmerror:
        print "VMMaintenence exception"

    # Disconnecting to Vcenter
    obj.disconnect(si)
