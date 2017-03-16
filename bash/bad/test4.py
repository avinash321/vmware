from pyVmomi import vim
import vmutils

# Connect to Vcenter
si=vmutils.connect()

host_name = raw_input("Enter the Host name: ")
host = vmutils.get_host_by_name(si, host_name)

host.ExitMaintenanceMode_Task(10)
print "Exit maintanence mode successfully"

# Disconnecting Vcenter
vmutils.disconnect(si)