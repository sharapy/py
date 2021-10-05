# freq = {}
# line = input()
# for word in line.split():
#     freq[word] = freq.get(word,0)+1

# words = freq.keys()
# words.sorted()
# for w in words:
#     print("%s:%d" % (w,freq[w]))
# ----***this doesnt work***---------

# Q23
# _______________________________________
# def square(num):
#     return num ** 2
# print(square(2))
# print(square(3))

# Q24
# _________________________________________

# print(abs.__doc__)
# print(int.__doc__)
# print(input.__doc__)

# def square(num):
#     ''' Return the square value of the input number.
#     The input number must be integer
#     '''
#     return num**2
# print(square(2))
# print(square.__doc__)

# Q25
# __________________________________________

# class Person:
#     # Define the class parameter "name"
#     name = "Person"
#     def __init__(self, name=None):
#         self.name=name

# jeffrey = Person("Jeffrey")
# print("%s name is %s" % (Person.name, jeffrey.name))

# nico = Person("Nico")
# # nico.name = "Nico"
# print("%s name is %s" % (Person.name, nico.name))

# Q31
# _________________________________________
# def printValue(s1, s2):
#     len1 = len(s1)
#     len2 = len(s2)
#     if len1>len2:
#         print(s1)
#     elif len2>len1:
#         print(s2)
#     else:
#         print(s1)
#         print(s2)
# printValue("one","three")

# Q27
# __________________________________________
