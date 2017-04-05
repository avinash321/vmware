'''
This will Reboot the given Esxi Host
'''
from vmware import VmwareLib
class RebootException(Exception):
   pass

def reboot(si, host_name, obj):
	host = obj.get_host_by_name(si, host_name)
	#This will Reboot the given Esxi Host
	if host:
		force = True
		obj.reboot_host(host, force)
    else:
        raise RebootException("Host error")

if __name__ == "__main__":

    # Creating Object for VMwareLib Class
    obj = VmwareLib()

    vcenter_ip = "183.82.41.58"
    username = "root"
    password = "VMware@123"

    # Connecting to Vcenter
    si = obj.connect(vcenter_ip, username, password)

    #Reboot operation
    host_name = "192.168.50.16"
    reboot(si, host_name, obj)

    # Disconnecting to Vcenter
    obj.disconnect(si)
