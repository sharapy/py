#Author: Sharad talekar
#Date: 24Jan2015
#Purpose: use of lists
import string

list1 = range(1,11) #returns range from 0 to 10
print list1
stringlist = ["Byte","of","Python"]
print stringlist
stringlist.reverse()
print stringlist

list1.reverse()
print list1

list1.extend(stringlist)
print list1
list1.insert(12,"100")
print list1

#Log files -----------------------

logfile = "24Jan2015 10.232.15.166 5060 10.203.200.136 486 request_cannot_be_completed"
# convert log file to a list from a stringlist
logfile2 = string.split(logfile)
print logfile2

#slice logfile2 to slash required fields

logfile3 = logfile2[0:5]
print logfile3

#?join logfile 3 to a flat string

logfile4 = string.join(logfile3)
print logfile4

