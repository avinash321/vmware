'''
This will Reboot the given Esxi Host
'''
from vmware import VmwareLib

def reboot(si, host_name):
	host = obj.get_host_by_name(si, host_name)
	#This will Reboot the given Esxi Host
	obj.reboot_host(host)


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
    reboot(si, host_name)

    # Disconnecting to Vcenter
    obj.disconnect(si)
