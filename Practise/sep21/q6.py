# Q51
# _________________________________
# class American(object):
#     pass
# class NewYorker(American):
#     pass
# anAmerican = American()
# aNewYorker = NewYorker()
# print(anAmerican)
# print(NewYorker)

# Q52
# _________________________________
# class Circle(object):
#     def __init__(self, r):
#         self.radius = r
#     def area(self):
#         return self.radius**2*3.14
# aCircle = Circle(2)
# print aCircle.area()

# Q53
# _________________________________
# class Shape(object):
#     def __init__(self):
#         pass
#     def area(self):
#         return 0
# class Square(Shape):
#     def __init__(self, l):
#         Shape.__init__(self)
#         self.length = l
#     def area(self):
#         return self.length*self.length
# aSquare = Square(3)
# print(aSquare.area())

# Q55
# ____________________________________

# raise RuntimeError('something wrong')

# Q56
# ____________________________________
# def throws():
#     return 5/0
# try:
#     throws()
# except ZeroDivisionError:
#     print("Division by zero!")
# except Exception:
#     print('Caught an exception')
# finally:
#     print('In finally block for cleanup')

# Q57
# _____________________________________
# class MyError(Exception):
#     """My own exception class
#     Attributes: 
#         msg -- explanation of the error
#     """
#     def __init__(self, msg):
#         self.msg = msg

# error = MyError("Something wrong")

# Q58
# _____________________________________
# import re
# emailAddress=input()
# pattern1 = "(\w+)@((\w+\.)+(com))"
# r = re.match(pattern1, emailAddress)
# print(r.group(1))

# Q60
# ______________________________________
# import re
# s = input()
# print(re.findall("\d+",s))

