#!/usr/bin/python
#Author: Sharad Talekar
#Date: 5thFeb2015
#Purpose: Practice Regular Expressions

import re

#reg1 = re.compile('hello', re.IGNORECASE) #Matches Verbatim
#reg1 = re.compile('\d', re.IGNORECASE) #Matches Verbatim
#reg1 = re.compile('\d+\s+\w+', re.IGNORECASE) #Matches digit/space/words

#reg1 = re.compile('\s+\w+@.*')
c=1
t=3 #to give 3 chances
print "Okay, you've got",t,"chances to make a match!"
while c <= t:
	searchstring = raw_input("Please give us a search string: ")
	match1 = reg1.match(searchstring) #Matches if string starts with re
	search1 = reg1.search(searchstring) #finds one occurrence of re	
	findall1 = reg1.findall(searchstring) #finds all occurrences of re and returns list
	finditer1 = reg1.finditer(searchstring) #iterates through all the occurrences of re
	if match1:
		print "Matched by match:\t", match1.group() 
	else:
		print "No Match!"
	if search1:
		print "Search Match:\t", search1.group()
	else:
		print "No Match"
	if findall1:
		print "Findall Match:\t", findall1
	else:
		print "No Findall match"
	if finditer1:
		for i in finditer1:
			print i.group()
	else:
		print "No find Iter match"
	c = c + 1
