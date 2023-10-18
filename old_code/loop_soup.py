#Author: Sharad Talekar
#Date: 27Jan2015
#Purpose: For loop and while loop

#!/usr/bin/python

REBikes = {"Thunderbird350":"Cruiser, 350cc, Rs1.31L",
			"Thunderbird500":"Cruiser, 500cc, Rs1.66L",
			"Classic350":"Classic, 350cc, Rs1.20L",
			"Classic500":"Classic, 500cc, Rs1.54L",
			"ContinentalGT":"CafeRacer,532cc, Rs1.88L",
			"Bullet350":"Bullet, 350cc, Rs1.04L",
			"Bullet500":"Bullet, 500cc, Rs1.44L",
			"DesertStorm":"Classic Matte brown, 500cc, Rs1.56L",
			"Electra":"Classic, 350cc, Rs1.14L"}

#for bike,price in REBikes.iteritems(): 
#	print bike,":",price
print "------------Royal Enfield 1.0----------------"	

while 1:
	i=1 #creating an index in other dictionary to choose Model ID
	bikeid = {} #initialization of new dictionary
	for bike in REBikes.keys():
		print "Model ID",i,": ",bike #print modelID and bike name
		bikeid[i] = bike #Create new dictionary bikeid
		i=i+1
	id = input("\n Select Model ID: ")
	user = bikeid[id] #extract bikename to check details in other dictionary
	print "-------------------------------------------------------"
	print user,":",REBikes[user] #Print result from main dictionary 
	print "-------------------------------------------------------"
	choice = raw_input("\n Do you wish to continue?")
	if choice == "yes" or choice == "Yes" or choice == "y":
		continue
	else:
		break 
#for x,y in bikeid.iteritems():
#	print x,y
	
