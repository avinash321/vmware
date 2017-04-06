def even_or_odd(n):
	if n % 2 == 0:
		return "Even Number"
	else:
		return "OddNumber"


if __name__ == "__main__":
	n = raw_input("Enter Your Number: ")
	while not n:
		n = raw_input("Please Enter Your Number: ")
	try:
		n = int(n)
		result = even_or_odd(n)
		print result
	except ValueError:
		print "Please Enter Only Numbers"
	except Exception as err:
		print err.message