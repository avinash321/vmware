''' this will  print the numbers below 5  for the given list'''

def list_below5(a):
	result = [i for i in a if i<5]
	return result


if __name__ == "__main__":
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	# this will fetch the elements below 5 from the list a
	result = list_below5(a)
	print result