''' Divisiors of a Number '''
def divisors(num):
	result = []
	for i in range(1,num+1):
		if num % i == 0:
			result.append(i)
	return result


if __name__ == "__main__":
	num = raw_input("Enter your Number: ")
	while not num:
		num = raw_input("Please Enter your Number: ")
	try:
		num =  int(num)
		result = divisors(num)
		print "The Divisors of "+ str(num) +" are: " + str(result)
	except ValueError:
		print "Please enter the number only"
	except Exception as err:
		print err.message




