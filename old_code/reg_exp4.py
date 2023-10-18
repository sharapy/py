#!/usr/bin/python
#Author: Sharad Talekar
#Date: 5thFeb2015
#Purpose: Practice Regular Expressions

import re

#reg1 = re.compile('hello', re.IGNORECASE) #Matches Verbatim
#reg1 = re.compile('\d+4', re.IGNORECASE) #Matches Verbatim
#reg1 = re.compile('\d+\s+\w+', re.IGNORECASE) #Matches digit/space/words

reg1 = re.compile('\w+@.*')
filename = "after1.txt"
file2 = "after2.txt"
f1 = open(filename,"r")
f2 = open(file2,"w")
for searchstring in f1.readlines():
	changes = reg1.sub("kuchbhi@sabkuch.com",searchstring, count=2) #sustitutes arg1 with RE at arg3 no of times in one line
	f2.writelines(changes)
	
f1.close()
f2.close()
	
	
	
