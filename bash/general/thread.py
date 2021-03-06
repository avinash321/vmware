#!/usr/bin/python

import thread
import time

# Define a function for the thread
def print_time1( threadName, delay):
   count = 0
   while count < 10:
      time.sleep(delay)
      count += 1
      print "%s: %s" % ( threadName, time.ctime(time.time()) )

def print_time2( threadName, delay):
   count = 0
   while count < 10:
      time.sleep(delay)
      count += 1
      print "%s: %s" % ( threadName, time.ctime(time.time()) )

# Create two threads as follows
try:
   thread.start_new_thread( print_time1, ("Thread-1", 2, ) )   
   thread.start_new_thread( print_time2, ("Thread-2", 4, ) )
except:
   print "Error: unable to start thread"

while 1:
   pass