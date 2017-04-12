def fibonacci(l):
	i =0
	while i > len(l):
		if l[i]+ l[i+1] == l[i+2]:
			i = i+1
		else:
			break
	return 1		
	

if __name__ == "__main__":
	s = raw_input("Enter your numbers , with comma seperation: ")
	while not s:
		s = raw_input("Enter your numbers , with comma seperation: ")
	try:
		l = s.split(',')
		l = map(lambda x:int(x), l)
		result = fibonacci(l)
		if result == 1:
			print "The given Number series is fibonacci series"
		else:
			print "The given Number series  is Not fibonacci series"
	except ValueError:
		print "Please Enter Numbers only, with comma seperation"
