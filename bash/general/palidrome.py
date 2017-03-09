k=raw_input("Enter your word:")
flag=""
n=len(k)-1
for i in k:
	flag=flag+k[n]
	n=n-1
if(flag == k):
	print "Polydrom"
else:
	print "not a Polydrom"


