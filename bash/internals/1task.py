'''
Date: 7th April 2017
Author: Avinash 
Description: This module will print the 100th year of a person based on his current age
'''

import datetime

def age_100_year(current_year, age_remain):
		year = current_year + age_remain
		return year

def current_year():
	try:
		now = datetime.datetime.now()
		year = now.year
		return year
	except Exception as err:
		print err.message

if __name__ == "__main__":
	name = raw_input("Enetr your name: ")
	while not name:
		name = raw_input("Please Enetr your name: ")
	age = raw_input("Enter your age: ")
	while not age:
		age = raw_input("Please Enter your age: ")

	try:
		age = int(age)
		if age<100 and age>0:
			age_remain = 100 - age
			# Getting the current Year
			current_year = current_year()
			output_year = age_100_year(current_year, age_remain)
			print  "Hello "+ name.upper() + ", you will turn 100 years old in the year " + '\033[1m' + str(output_year) + '\033[0m'
		else:
			print "please Enter the age beween(1 t0 99)"
	except ValueError:
		print "please Enter the age as Numeric Number"
	except Exception as err:
		print err.message









