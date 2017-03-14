import time
f=open("/home/nexii/abc.txt",'r')
for i in range(100):
	print f.readlines()
	time.sleep(1)
