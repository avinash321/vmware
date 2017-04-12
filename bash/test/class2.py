import re
f = open("/home/nexii/file1.txt")
k = f.read()

print re.findall(".",k)

