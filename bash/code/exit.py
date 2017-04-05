'''
This will put the given Esxi Host into maintanence mode
'''
from vmware import VmwareLib
def maintanencemode(si, host_name, obj):
    host = obj.get_host_by_name(si, host_name)
    timeout = 3000
    # 3000 secends
    # This will put the given Esxi host in maintanence mode
    if host:
       obj.exit_maintanence_mode(host, timeout)

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
    maintanencemode(si, host_name, obj)

    # Disconnecting to Vcenter
    obj.disconnect(si)
