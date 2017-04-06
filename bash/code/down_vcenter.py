import paramiko
ssh=paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)  
#ssh.set_missing_host_key_policy(paramiko.WarningPolicy)
def connect():
	try:
		conn = ssh.connect("192.168.50.14",port=22,username="roo",password="Avinash")
		print "Connected Successfully"
	except Exception as err:
		print err

def vcenter_down():
	try:
		stdin,stdout,strerr=ssh.exec_command('shutdown -r +5 "Server will restart in 5 minutes. Please save your work."')
		# shutdown -h now     (immidiate Shutdown)
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




