print "this program is helpful to know the provided tiffins based on the day "
t1={'monday':'idly','tuesday':'dosa','wednesday':'upma','thursday':'chapathi',
'friday':'lemon rice','saturday':'wada','sunday':'puri'}
print "Enter 1 to know the tiffin based on given day: "
print "Enter 2 to know the day based on tiffins: "
f1=input("enter your choice here: ")

#This is to know the Day 
if f1==1:
	print "The Avilable tiffins are: "
	l1=t1.values()
	l1.sort()
	for i in range(len(l1)-1):
		print l1[i]
	k1=raw_input("enter your tiffin Here: ")


	
#This is to know the Tiffin

if f1==2:
	print "Enter the day to know the tiffin on that day: "
	l1=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
	for i in range(len(l1)-1):
		print l1[i]
	k1=raw_input("enter your Day Here: ")
	out=t1.get(k1)
	print "the tiffin on "+k1.upper()+" is "+out.upper()

