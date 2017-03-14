import time

def print_diamond():
	for i in range(1,6):
		for j in range(1,6):
			if (i+j == 4 or i+j == 8 or i-j == 2 or j-i== 2):
				print "*",
				time.sleep(0.2)
			else:
				print " ",
		print ""

for i in range(1,11):
	for j in range(1,11):
		if (j==5 or i==5):
			print "*",
		else:
			print " ",
		time.sleep(0.05)
	print ""


