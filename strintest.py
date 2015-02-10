#Author: Sharad Talekar
#Date: 20-Jan-2015
#Purpose: String works

import string

message = "Barney is waiting"
message2 = "Barney likes to go out"
product = "barney the lhasa apso"

print message
print "String ",message, "contains", len(message), "characters"
print "First character in",message, "is", message[0]
print "First word in",message, "is", message[0:6] 
for letter in message:
	print letter
if message == message2:
	print "They Match!"
else: print "Message 2 is: ", message2

message = string.upper(message)
print message

message = string.lower(message)
print message

print string.capitalize(message)
print string.capwords(message)
print string.split(message)
print string.join(message)

print string.capwords(product)

raw_input("Do you know who is Barney?\n")





