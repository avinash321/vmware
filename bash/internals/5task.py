 
'''This will print the comman values from the given two lists'''
def common_list(a,b):
	result = []
	for i in a:
		for j in b:
			if i == j:
				if i not in result:
					result.append(i)
	return result


if __name__ == "__main__":
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
 	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
 	result = common_list(a,b)
 	print "the comman values from the given two lists are: "+ str(result)
