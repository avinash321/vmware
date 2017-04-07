import random
def random_num():
	num = random.randrange(1,9)
	return num


if __name__ == "__main__":
	while True:
		try:
			rand_num = random_num()
			num = raw_input("Guess the Number that going to print between 1 to 9: ")
			while not num:
				num = raw_input("Guess the Number that going to print between 1 to 9: ")
			num = int(num)
			if num>0 and num<10:
				if num == rand_num:
					print "The number you entered is: " + str(num)
					print "The actual number is: " + str(rand_num)
					print "You guessed CORRECT"
				else:
					print "The number you entered is: " + str(num)
					print "The actual number is: " + str(rand_num)
					print "you guessed WRONG"
			else:
				print "Please enter the number between 1 to 9"
		except ValueError:
			print "Please Enter number onnly"
		except Exception as err:
			print err.message
