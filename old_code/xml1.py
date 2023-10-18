import xml.etree.ElementTree as etree
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element


#Define our data file
#data_file = 'test.xml'

#if os.path.exists(data_file) != True:
#    fh1 = open(data_file,"a")
#    fh1.write("<list>\n</list>")
#    fh1.close()
#else:
#    print("booo!")


#---------------------------------------------
#New code for Etree
root = Element('person')
tree = ElementTree(root)
name = Element('name')
root.append(name)
name.text='Shady'
root.set('id','123')
#print(etree.tostring(root))
tree.write(open("person.xml","w"))

