#!/usr/bin/python

import pickle
import os
contactFile = 'contactFile.data'

class ContactInfo:
  contacts = {}
  def __init__(self,name):
    self.name = name
  def addContact(self, info):
    ContactInfo.contacts[self.name] = info
  def modContact(self, key, info):
    if key in ContactInfo.contacts.keys():
      ContactInfo.contacts[key] = info
    else: print "Contact not found....!"
  def delContact(self, key):
    if key in ContactInfo.contacts.keys():
    del ContactInfo.contacts[key]
    else: print "Contact not found....!"
  def searchContact(self, key):
    if key in ContactInfo.contacts.keys():
      print "------search result-----"
      print key,": ",ContactInfo.contacts[key]
      print "------------------------"
    else: print "Contact not found....!"

if os.path.exists('/root/Documents/sharad/contactFile.data'):
  f = open(contactFile,'rb')
  ContactInfo.contacts = pickle.load(f)
  f.close()
else: pass

while(1):
  print "1: Add Contact\n2: Update Contact\n3: Remove Contact\n4: Search contact\n5: List contacts"
  option = input("Choose option: ")
  if option == 1:
    cname = raw_input("Enter name: ")
    ob = ContactInfo(cname)
    cinfo = raw_input("Enter number: ")
    ob.addContact(cinfo)
    #print ob.contacts
    continue
  elif option == 2:
    key = raw_input("Enter contact to update:")
    ob = ContactInfo(key)
    cinfo = raw_input("update contact(csv):")
    ob.modContact(key, cinfo)
    #print ob.contacts
    continue
  elif option == 3:
    key = raw_input("Enter contact name to delete: ")
    ob = ContactInfo(key)
    ob.delContact(key)
    #print ob.contacts
    continue
  elif option == 4:
    key = raw_input("Enter the contact to search: ")
    ob = ContactInfo(key)
    ob.searchContact(key)
    continue
  elif option ==5:
    ob = ContactInfo.contacts
    print "-------All Contacts------"
    for k,v in ContactInfo.contacts.iteritems():
      print k,": ",v
      print "-------------------------"
  else:
    break
f = open(contactFile,'wb')
pickle.dump(ContactInfo.contacts,f)
f.close()

print "----------End------------"
