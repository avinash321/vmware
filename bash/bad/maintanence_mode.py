import vmutils

# Connect to Vcenter
si = vmutils.connect()

host_name = raw_input("Enter the Host name: ")
host = vmutils.get_host_by_name(si, host_name)

def enter_maintanence_mode(host):
	host.EnterMaintenanceMode_Task(3000)
	print "Enter maintanence mode successfully"


def exit_maintanence_mode(host):
	host.ExitMaintenanceMode_Task(10)
	print "Exit maintanence mode successfully"


if __name__ == "__main__":
	exit_maintanence_mode(host)

# Disconnecting Vcenter
vmutils.disconnect(si)
