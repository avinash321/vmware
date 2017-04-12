import paramiko
ssh=paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)  
#ssh.set_missing_host_key_policy(paramiko.WarningPolicy)
def connect():
	try:
		conn = ssh.connect("192.168.50.18",port=22,username="root",password="Nexii@123")
		print "Connected Successfully"
	except Exception as err:
		print err
def vcenter_down():
	try:
		stdin,stdout,strerr=ssh.exec_command("ls -l")
		# shutdown -h +5 "Server is going down for upgrade. Please save your work."
		#(shutdown with 5min Delay)
		output=stdout.readlines()
		print output
	except Exception as err:
		print err.message

def disconnect():
	try:
		close = ssh.close()
		print "DisConnected Successfully"
	except Exception as err:
		print err.message

if __name__ == "__main__":
	connect()
	vcenter_down()
	disconnect()