#!/usr/bin/python
#Author: sharad Talekar
#Date: 4 Feb 2015
#Purpose: To practice File IO and Exceptions
import os

while 1:

	file1 = input("Enter the file name :")
	try:
		fh1 = open(file1,"r")
		break
	except:
		print ("Could not open file :", file1)
		print ("Re-",)
		continue
		
while 1:	
	file2 = input("Enter the new file name: ")
	try:
		fh2 = open(file2,"w")
		break
	except:
		print ("Cannot write to :", file2)
		continue
temp = fh1.readlines()
fh2.writelines(temp) 

path = os.system('chdir')
print ("File copied at ", 'path')

fh1.close()
fh2.close()

