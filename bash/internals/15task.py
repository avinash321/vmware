def reverse(s):
	l = s.split()
	l.reverse()
	return " ".join(l)
	

if __name__ == "__main__":
	s = "my name is avinash"
	result  = reverse(s)
	print result

