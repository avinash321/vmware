'''
This will put the given Esxi Host into maintanence mode
'''
from vmware import VmwareLib
class VMMaintenceException(Exception):
    pass

def maintanencemode(si, host_name, obj):
    host = obj.get_host_by_name(si, host_name)
    # This will put the given Esxi host in maintanence mode
    if host:
        timeout = 3000   # 3000 secends
        obj.enter_maintanence_mode(host, timeout)
    else:
        raise VMMaintenceException("Host Not Found")

if __name__ == "__main__":

    # Creating Object for VMwareLib Class
    obj = VmwareLib()

    vcenter_ip = "183.82.41.58"
    username = "root"
    password = "Nexii@123"

    # Connecting to Vcenter
    si = obj.connect(vcenter_ip, username, password)
    if si:
        #Reboot operation
        host_name = "192.168.50.22"
        try:
            maintanencemode(si, host_name, obj)
        except VMMaintenceException as vmerror:
            print vmerror.message
            print "VMMaintenence exception"

        # Disconnecting to Vcenter
        obj.disconnect(si)
