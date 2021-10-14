# Sum of elements in Array

# def sumArray(a):
#     sum = 0
#     for each in a:
#         sum = sum + each
#     return sum
# a = [1,1,43,1,3,5,12]
# print(sumArray(a))
# -------------- using in built
# print(sum(a))
# ------------------------------Largest element in list
# def largest(arr,n):
#     max = arr[0]
#     for i in range(1,n):
#         if arr[i] > max:
#             max = arr[i]
#     return max
# arr = [2,6,32,41,8,14,16,42,32]
# l = len(arr)
# print("largest in given array is",largest(arr,l))
# one more one liner
# print(sorted(arr)[l-1])
#-------------------------------- array rotation
#by slicing
# def rotateList(arr,d,n):
#     arr[:] = arr[d:n] + arr[0:d]
#     return arr
# arr = [2,6,32,41,8,14,16,42,32]
# print(arr)
# print("Rotated list",rotateList(arr,3,len(arr)))

#--------------------------------- 
# by reverseList
# def reverseList(arr, start, end):
#     while(start<end):
#         temp = arr[start]
#         arr[start] = arr[end]
#         arr[end] = temp
#         start += 1
#         end -= 1

# def leftRotate(arr,d):
#     if d==0:
#         return
#     n = len(arr)
#     d = d%n
#     reverseList(arr,0,d-1)
#     reverseList(arr,d,n-1)
#     reverseList(arr,0,n-1)
# arr = [1,2,3,4,5,6,7]
# n= len(arr)
# d=2
# leftRotate(arr,d)
# print(arr)

# ------------------------------------multipication divide by n
from functools import reduce
def find_remainder(arr,n):
    sum1 = reduce(lambda x,y: x*y, arr)
    print(sum1)
    remainder = sum1 % n
    print(remainder)

arr = [100,10,5,25,35,14]
n=11
find_remainder(arr,n)
print((arr))
