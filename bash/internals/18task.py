import random
def cows_bulls(cow,bull):
	i = 0
	while i<len(n):
		j=0
		while j<len(number):
			if n[i] ==  number[j] and i==j:
				cow = cow+1
			elif n[i] ==  number[j]:
				bull = bull+1
			j = j+1
		i = i+1
	return cow , bull

def random_num():
	num = random.randint(1000,9999)
	return num


if __name__ == "__main__":
	n = raw_input("Enter Your 4 digit Number: ")
	while not n:
		n = raw_input("Enter Your 4 digit Number: ")
	if len(n)>4 or len(n) <4:
		print "please enter 4 Digit Number"
	else:
		try:
			n = int(n)
			n = str(n)
			print "The Given Number: "+ n
			number = random_num()
			number = str(number)
			print "The Generated Number: " + number
			cow = 0
			bull = 0
			result = cows_bulls(cow,bull)
			print "Cows: " + str(result[0])
			print "Bulls: " + str(result[1])
		except ValueError:
			print "Please Enter Number Only"
		except Exception as err:
			print err

