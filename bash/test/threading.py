import time
from threading import Thread
class A(Thread):
	def run(self):
		for i in range(1,101):
			print i

class B(Thread):
	def run(self):
		for j in range(101,201):
			print j

k1= A()
k2 = B()

k1.start()
k2.start()