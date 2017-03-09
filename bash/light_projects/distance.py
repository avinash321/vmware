print "Hi , this program is helpful to findout the distance betwen the two locations"

d1={'aler':0,'wangapalli':12,'raigir':18,'bhongir':25,'bibinagar':37,'gatkesar':52,'Uppal':60,'Hyderabad':70}
l1=['aler','wangapalli','raigir','bhongir','bibinagar','gatkesar','uppal','hyderabad']

print "please choose your from and to locationsfrom the following: "
print "The available locations are: "
for i in range(len(l1)-1):
	print l1[i]
from_location=raw_input("Enter From Location: ")
to_location=raw_input("Enter to location: ")
distance=0
k1=d1.get(from_location)
k2=d1.get(to_location)
if k1>k2:
	distance=int(k1)-int(k2)
else:
	distance=int(k2)-int(k1)
print "the distance between "+from_location+ " and " +to_location+ " is: "+ str(distance) + "kms"