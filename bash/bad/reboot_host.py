'''
Script for: Rebooting or shut down the ESXI Host
Reboot or Shut Down an ESXi Host
You can power off or restart (reboot) any ESXi host using the vSphere Client. Powering off a managed host disconnects it from vCenter Server, but does not remove it from the inventory.
Procedure
1 Shut down all virtual machines running on the ESXi host.
2 Select the ESXi host you want to shut down.
3 From the main or right-click menu, select Reboot or Shut Down.
■ If you select Reboot, the ESXi host shuts down and reboots.
■ If you select Shut Down, the ESXi host shuts down. You must manually power the system back on.
4 Provide a reason for the shut down.
This information is added to the log.
'''
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