try:
	s="dfdsddd"
	s.replace('a')
	print x
except ZeroDivisionError:
	print "This is ZeroDivisionError"
except TypeError:
	print "this is Type Error"
except ValueError:
	print "this is value error"
except IndexError:
	print "Given Index Is out of range"

