'''
This will put the given Esxi Host into maintanence mode
'''

from vmware import VmwareLib

# Creating the object for vmwareLib class
obj = VmwareLib()

# Connecting to Vcenter Server
si = obj.connect()

host_name = raw_input("Enter the Host name: ")
host = vmutils.get_host_by_name(si, host_name)

# This will put the given Esxi host in maintanence mode
obj.enter_maintanence_mode(host)

# Disconnecting form Vcenetr
obj.disconnect(si)
