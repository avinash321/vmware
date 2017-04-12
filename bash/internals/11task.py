
def check_prime(n):
	for i in range(2,n):
		if n%i == 0:
			return -1
			break

if __name__ == "__main__":
	n = raw_input("Enter your number: ")
	while not n:
		n = raw_input("Please Enter your number: ")
	try:
		n = int(n)
		result = check_prime(n)
		if result == -1:
			print str(n) + " is Not a Prime Number"
		else:
			print str(n) + " Is a Prime Number"
		
	except ValueError:
		print "Please Enter Number Only"
	except Exception as err:
		print err.message

