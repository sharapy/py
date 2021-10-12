# value = []
# items=[x for x in input().split(',')]
# for p in items:
#     intp = int(p, 2)
#     if not intp%5:
#         value.append(p)

# print(','.join(value))

# Q12
# ___________________________
# values = []
# for i in range(1000,3001):
#     s=str(i)
#     if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
#         values.append(s)
# print(",".join(values))

# Q13
# ____________________________
# s= input()
# d = {"DIGITS":0, "LETTERS":0}
# for c in s:
#     if c.isdigit():
#         d["DIGITS"]+=1
#     elif c.isalpha():
#         d["LETTERS"]+=1
#     else:
#         pass
# print(d)

# Q14
# _____________________________
# s = input()
# d = {"UPPER CASE":0, "LOWER CASE": 0}
# for c in s:
#     if c.isupper():
#         d["UPPER CASE"]+=1
#     elif c.islower():
#         d["LOWER CASE"]+=1
#     else:
#         pass
# print(d)

# Q15
# ______________________________
# a = input()
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a))
# n3 = int( "%s%s%s" % (a,a,a))
# n4 = int( "%s%s%s%s" % (a,a,a,a))
# print(n1+n2+n3+n4)
# print(n1,n2,n3,n4)

# Q16
# ______________________________
# values = input()
# numbers = [x for x in values.split(",") if int(x)%2!=0]
# print(",".join(numbers))

# Q17
# _______________________________
# netAmount = 0
# while True:
#     s = input()
#     if not s:
#         break
#     values = s.split(" ")
#     operation = values[0]
#     amount = int(values[1])
#     if operation =="D":
#         netAmount+=amount
#     elif operation =="W":
#         netAmount-=amount
#     else:
#         pass
# print(netAmount)

# Q18
# _______________________________
# import re
# value = []
# items = [x for x in input().split(',')]
# for p in items:
#     if len(p)<6 or len(p)>12:
#         continue
#     else:
#         pass
#     if not re.search("[a-z]",p):
#         continue
#     elif not re.search("[0-9]",p):
#         continue
#     elif not re.search("[A-Z]",p):
#         continue
#     elif not re.search("[$#@]",p):
#         continue
#     elif re.search("\s",p):
#         continue
#     else:
#         pass
#     value.append(p)
# print(",".join(value))

# Q 19
# ____________________________
# from operator import itemgetter
# l = []
# while True:
#     s = input()
#     if not s:
#         break
#     l.append(tuple(s.split(',')))

# print(sorted(l, key=itemgetter(0,1,2)))

# Q20
# ______________________________
# def putNumbers(n):
#     i=0
#     while i<n:
#         j=1
#         i=i+1
#         if j%7==0:
#             yield j
# for i in reverse(100):
#     print(i)