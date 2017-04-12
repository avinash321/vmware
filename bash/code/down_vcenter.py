import paramiko
ssh=paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)  
#ssh.set_missing_host_key_policy(paramiko.WarningPolicy)
import logging
logging.basicConfig(filename="log_Esxi_maintanence_mode.txt",level=logging.DEBUG,
format = "%(asctime)s-->%(levelname)s-->%(message)s")

def connect(ip, port_num, uid, pwd):
	try:
		conn = ssh.connect(ip, port=port_num, username=uid, password=pwd)
		return conn
	except Exception as err:
		print err.message

def vcenter_down():
	try:
		stdin,stdout,strerr=ssh.exec_command('ls')
		# shutdown -h now     (immidiate Shutdown)
		# shutdown -h +5 "Server is going down for upgrade. Please save your work."
		# shutdown -r +5 "Server will restart in 5 minutes. Please save your work."
		output=stdout.readlines()
		return output
	except Exception as err:
		print err.message

def disconnect():
	try:
		close = ssh.close()
		return close
	except Exception as err:
		print err.message

def main():
	ip = "192.168.50.14"
	port  = 22
	username = "root"
	password = "Avinas"
	conn = connect(ip, port, username, password)
	if conn:
		loggr.info("connection successful")
		result = vcenter_down()
		logger.debug(result)
		logger.info("Command Exceuted")
		close  = disconnect()
		logger.debug(close)

if __name__ == "__main__":
	main()






