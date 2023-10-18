#Author: Sharad Talekar
#Date: 26th Jan 2015
#Purpose: Learning Python Conditionals

#!/usr/bin/python

	
#----------------which bike---------------
print "-----------ADV Bike Chooser 1.0 ---------------"
versys650 = {"Speed":120,"engine":"SingleCylinder","tank":"17L","Price":"$7999"}
vstorm = {"Speed":170,"engine":"DoubleCylinder","tank":"22L","Price":"$8549"}

#print versys650
#print vstorm

import string

custname = raw_input("What is your name? ")
print "What kind of engine would you like?"
custengine = raw_input("SingleCylinder or DoubleCylinder :")
custtank = raw_input("What should be the tank Capacity? ")

print "Customer Requirement: ",custname,"\nEngine Type: ",custengine,"\nTank Capacity: ",custtank

if custengine == "single" and custtank <= "17":
	print "\nVersys650 is the one!"
	for k,v in versys650.iteritems():
		print k,": ",v
		
elif custengine == "double" and custtank <= "22":
	print "\nVStorm is the one!"
	for k,v in vstorm.iteritems():
		print k,": ",v
		
else:
	print "\nSorry",custname,", none of the bikes match your requirement"
	
