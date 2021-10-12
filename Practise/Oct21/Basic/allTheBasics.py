# Sum it up
# num1 = 2
# floatnum1 = input("Enter float 1: ")
# floatnum2 = input("Enter float 2: ")
# num2 = 4
# sum = num1 + num2
# fsum = float(floatnum1) + float(floatnum2)
# print("Sum of {} and {} is: {}".format(num1, num2, sum))
# print("Sum of floats, {} and {} is: {}".format(floatnum1, floatnum2, fsum))
# -----------------------------------------------
# Factorial of a number
#1 Recursive 
# def factorial(n):
#     return 1 if (n==1 or n==0) else n * factorial(n-1)
# n = 6
# print("Factorial of",n,"is",factorial(n))
# ___________________________________
#2 Iterative
# def factorial(n):
#     if n<0:
#         return 0
#     elif n==0 or n==1:
#         return 1
#     else:
#         fact = 1
#         while(n>1):
#             fact *= n
#             n -= 1
#         return fact
# n = 0
# print("Factorial:",n,"is",factorial(n))
# __________________________________________
#3 Built-in
# import math
# def factorial(n):
#     return(math.factorial(n))
# num = 6
# print("Factorial of num",num,"is",factorial(num))

# ---------------------------------------------
# Simple interest program
# def simple_interest(p,t,r):
#     print("Principle:", p)
#     print("Time:", t)
#     print("Rate", r)

#     si = (p*t*r)/100
#     print("Simple interest is ", si)
# simple_interest(10000,12,5)

# -----------------------------------------Max of 2nums
# def maximum(a,b):
#     if a>=b:
#         return a
#     else:
#         return b
# a=2; b=4
# print(maximum(a,b))
# ---------------using inBuilt
# print(max(a,b))
# -----------------using Ternary
# print(a if a>=b else b)

#___________________________________Compound Interest
# def compound_interest(principle, rate, time):
#     Amount = principle * (pow((1 + rate/100), time))
#     CI = Amount - principle
#     print("Compound interest is", CI)
# compound_interest(1200,5.4,2)

# ------------------------------------Armstrong number
# x=153
# l = len(str(x))
# xl = str(x)
# total1 = 0
# for a in xl:
#     ap = pow(int(a),l)
#     total1 = total1 + ap
# print("x is {}, value is {} ".format(x,total1))
# if x==total1:
#     print("True")
# else: print("False")

# -------------------------------Area of Circle
# def findArea(r):
#     PI = 3.142
#     return PI * pow(r,2)
# print("Area of Circle: %.3f" % findArea(5))
# --------------------------------Prime Numbers
# start = 11
# end = 25
# for i in range(start, end+1):
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(i)
#---------------------------------Prime or not
# def isItPrime(n):
#     if n>1:
#         for i in range(2, int(n/2)+1):
#             if n%i == 0:
#                 print("its not prime")
#                 break
#         else:
#             print("its prime")
#     else:
#         print("its not prime")
# isItPrime(21)

# -------------------------------- fibonacci sequence
# def fibonacci(n):
#     if n==1:
#         return 1
#     elif n==2:
#         return 1
#     elif n>2:
#         return fibonacci(n-1) + fibonacci(n-2)

# for n in range(1,11):
#     print(n, ":", fibonacci(n))

# --------------------------------- fibonacci memoization
# fibonacci_cache = {}
# def fibonacci(n):
#     if n in fibonacci_cache:
#         return fibonacci_cache[n]
#     if n==1:
#         value = 1
#     elif n==2:
#         value = 1
#     elif n>2:
#         value = fibonacci(n-1) + fibonacci(n-2)
#     fibonacci_cache[n] = value
#     return value
# for n in range(1,101):
#     print(n,":", fibonacci(n))

# ---------------------------------- fibonacci using lru_cache
# from functools import lru_cache

# @lru_cache(maxsize=1000)
# def fibonacci(n):
#     if n==1: return 1
#     elif n==2: return 1
#     elif n>2: return fibonacci(n-1) + fibonacci(n-2)

# for n in range(1,51):
#     print(n,":",fibonacci(n))

#---------------------------------- nth multiple of x in fibonacci
# def fibonacci(n):
#     if n==1: return 1   
#     elif n==2: return 1
#     elif n>2: return fibonacci(n-1) + fibonacci(n-2)
# p = 3
# x = 2
# mul_vals = []
# pos = []
# for n in range(1,21):
#     val = fibonacci(n)
#     if fibonacci(n)%x == 0: 
#         mul_vals.append(val)
#         pos.append(n)
# print(mul_vals[p-1],"appears at position",pos[p-1])

# ---------------------------- ASCII value of character
# char = "g"
# print("ASCII of ",char,'is',ord(char))
#-----------------------------Sum of square of n natural numbers

# def squaresum(n):
#     sm = 0
#     for i in range(1,n+1):
#         sm = sm + (i*i)
#     return sm
# n = 5
# print(squaresum(n))
# -----------------------------sum of cube of n
# def cubesum(n):
#     cube = 0
#     for i in range(0,n+1):
#         cube = cube + pow(i,3)
#     return cube
# n = 7
# print(cubesum(n))

# -----------------------------