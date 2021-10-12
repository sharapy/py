# l = []
# for i in range(2000, 3201):
#     if (i%7==0) and (i%5!=0):
#         l.append(str(i))

# print(','.join(l))

# Q2
# def fact(x):
#     if x==0:
#         return 1
#     return x * fact(x-1)
# x=int(input())
# print(fact(x))

# Q3
# -----------------
# n=int(input())
# d={}
# for i in range(1,n+1):
#     d[i]=i*i
# print(d)

# Q4
# _________________
# values=input()
# l=values.split(",")
# t=tuple(l)
# print(l)
# print(t)

# Q5
# ________________________
# class InputOutString(object):
#     def __init__(self):
#         self.s = ""
#     def getString(self):
#         self.s = input()
#     def printString(self):
#         print(self.s.upper())

# strObj = InputOutString()
# strObj.getString()
# strObj.printString()

# Q6
# ____________________________
# import math
# c=50
# h=30
# value = []
# items = [x for x in input().split(',')]
# for d in items:
#     value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
# print(','.join(value))

# Q7
# ____________________________
# input_str = input()
# dimensions=[int(x) for x in input_str.split(',')]
# rowNum = dimensions[0]
# colNum = dimensions[1]
# multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
# print(multilist)

# for row in range(rowNum):
#     for col in range(colNum):
#         multilist[row][col] = row*col

# print(multilist)

# Q8
# -----------------------------
# items=[x for x in input().split(',')]
# items.sort()
# print(','.join(items))

# Q9
# ------------------------------
# lines = []
# while True:
#     s=input()
#     if s:
#         lines.append(s.upper())
#     else:
#         break;

# for sentence in lines:
#     print(sentence)

# Q10
# -----------------------------
# s = input()
# words = [word for word in s.split(" ")]
# print(" ".join(sorted(list(set(words)))))

