import paramiko
ssh=paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)  
#ssh.set_missing_host_key_policy(paramiko.WarningPolicy)
def connect():
	try:
		conn = ssh.connect("192.168.50.14",port=2222,username="root",password="Avinash")
		print "***connecting......****"
		return conn
	except Exception as err:
		print err
		return None

def disconnect():
	try:
		ssh.close

def vcenter_down():
	try:
		stdin,stdout,strerr=ssh.exec_command('more /etc/sysconfig/selinux')
		output=stdout.readlines()
		print output
except Exception as err:
	print err

ssh.close()