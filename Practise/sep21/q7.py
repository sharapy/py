# unicodeString = u"hello world!"
# print(unicodeString)

# Q64
# _______________________________
# n = int(input())
# sum = 0.0
# for i in range(1,n+1):
#     sum+=float(float(i)/(i+1))
# print(sum)

# Q65
# _______________________________
# def f(n):
#     if n==0:
#         return 0
#     else:
#         return f(n-1)+100
# n=int(input())
# print(f(n))

# Q66
# Fibonacci ______________________
# def f(n):
#     if n==0: return 0
#     elif n==1: return 1
#     else: return f(n-1)+f(n-2)
# n = int(input())
# values = [str(f(x)) for x in range(0,n+1)]
# print(",".join(values))

# Q68
# ______________________________________
# def EvenGenerator(n):
#     i=0
#     while i<n:
#         if i%2==0:
#             yield i
#         i+=1
# n=int(input())
# values=[]
# for i in EvenGenerator(n):
#     values.append(str(i))

# print(",".join(values))


