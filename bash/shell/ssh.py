import paramiko
ssh=paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)  
#ssh.set_missing_host_key_policy(paramiko.WarningPolicy)
ssh.connect("192.168.50.14",port=22,username="root",password="Avinash")
print "***connecting......****"
#--------------------------------------------------------------------------------------------------------
#Executing Check RHEL OS Version
# RHEL types
support_os=["CentOS","Asianux","ClearOS","Fermi Linux LTS","Miracle Linux","Oracle Linux",
"Red Flag Linux","Rocks Cluster Distribution","Scientific Linux","SME Server"]
stdin,stdout,strerr=ssh.exec_command('cat /etc/redhat-release')
output=stdout.readlines()
out=output[0]
k = out.split(" ")
res=k[0]
count=0
print res
for i in support_os:
	if(i == res):
		count += 1
if(count>0):
	print "OS Version will support"
else:
	print "OS version will not support"

#----------------------------------------------------------------------------------------------------------
#disable selinux
stdin,stdout,strerr=ssh.exec_command('more /etc/sysconfig/selinux')
output=stdout.readlines()
print output
ssh.close()