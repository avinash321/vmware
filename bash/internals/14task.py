def remove_duplicates(l):
	l1 = []
	[l1.append(i) for i in l if i not in l1]
	return l1

if __name__ == "__main__":
	l = [1,2,3,4,1,2,5,6,7,4,6,7,8,8,9,5,4,3,2,6,7,33,44,22,3,33,44]
	result = remove_duplicates(l)
	print result
	

