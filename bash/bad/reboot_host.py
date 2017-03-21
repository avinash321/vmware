
import vmutils

si = vmutils.connect()

host_name = raw_input("Enter the Host name: ")
host = vmutils.get_host_by_name(si, host_name)


def reboot_host(host):
	host.RebootHost_Task(True)
	print "Rebooted the Host successfully"

def shut_down_host(host):
	host.ShutdownHost_Task(True)
	print "Shutdown the Host successfully"

if __name__ == "__main__":
	reboot_host(host)

vmutils.disconnect(si)