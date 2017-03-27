'''
This will Reboot the given Esxi Host
'''

from vmware import VmwareLib

# Creating the object for vmwareLib class
obj = VmwareLib()

# Connecting to Vcenter Server
si = obj.connect()

host_name = raw_input("Enter the Host name: ")
host = vmutils.get_host_by_name(si, host_name)

#This will Reboot the given Esxi Host
obj.reboot_host(host)

# Disconnecting form Vcenetr
obj.disconnect(si)
