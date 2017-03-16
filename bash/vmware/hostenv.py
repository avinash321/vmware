import vmutils

def get_host_by_name(si ,name):
	# Root Folder
	content=si.content
	rootfolder=content.rootFolder

	#DataCenter
	datacenters=rootfolder.childEntity
	datacenter=datacenters[1]

	#Host Folder
	hostfolder = datacenter.hostFolder
	domains = hostfolder.childEntity

	# Getting the Host
	domain = domains[0]
	host = domain.host[0]

	return host

def enter_maintanence_mode(host):
	host.EnterMaintenanceMode_Task(3000)
	print "Enter maintanence mode successfully"


def exit_maintanence_mode(host):
	host.ExitMaintenanceMode_Task(10)
	print "Exit maintanence mode successfully"
# # Putting the Host into Maintanence mode

if __name__ == "__main__":
	si = vmutils.connect()
	host_name = raw_input("Enter the Host name: ")
	host = get_host_by_name(si ,host_name)

	exit_maintanence_mode(host)

	vmutils.disconnect(si)
