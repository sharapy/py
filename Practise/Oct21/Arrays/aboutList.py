# Swap two elements in a list 
# def swapPosition(list1, pos1, pos2):
#     list1[pos1], list1[pos2] = list1[pos2], list1[pos1]
#     return list1
# list1 = [10,24,54,68,67,78] 
# print(swapPosition(list1,pos1=2,pos2=5))
# --------------------------------------------if element exist in list
# list1 = [12,5,8,4,6,7,14]
# if 8 in list1:
#     print("success")
# --------------------------------------------Clear list
# x = [1,2,4,5,4]
# print(x)
# x.clear()
# print(x)
# also can be multiplied by 0
# del x[:] #Delete every element
# ------------------------------------------reverse list
# x = [1,2,4,5,4]
# b = x[::-1] # method1
# print(b) 
# print([ele for ele in reversed(list(x))]) # method2
# ------------------------------------------ multiply all the values in list
# def multiplyList(myList):
#     result = 1
#     for x in myList:
#         result = result * x # method1
#     return result
# x = [1,2,4,5,4]
# print(multiplyList(x))

# from functools import reduce
# list1 = reduce((lambda a,b: a*b), x) # method 2
# print(list1)

# ------------------------------------smallest element in list
# arr = [2,5,4,8,9,6,1]
# print(sorted(arr)[0])
# print(min(arr))
# -----------------------------------largest number in list 
# print(sorted(arr)[-1])
# print(max(arr))
# -------------------------------------second largest in list
# print(sorted(arr)[-2])
#----------------------------------N largest numberes in list
# l = [12,54,9,8,6,5,7,4,6,87,64,5,7,6,4,8,5]
# n =4
# print(sorted(l)[-n:])
#----------------------------------even nos in a list
# list1 = [12,54,9,8,6,5,7,4,6,87,64,5,7,6,4,8,5]
# even_nos = [num for num in list1 if num % 2 == 0]
# print(even_nos)
#----------------------------------even nos in given range
# x=2; y=30
# even_nos = [num for num in range(x,y) if num%2==0]
# print(even_nos)
#----------------------------------- print positive nos
# list1 = [12,-54,-9,8,6,5,-7,4,6,-87,64,5,7,6,4,8,5]
# pos_nos = [num for num in list1 if num > 0]
# print(pos_nos)
# ---------------------------------- duplicate in list
# l=[1,2,3,4,5,2,3,4,7,9,5]
# l1=[]
# for i in l:
#     if i not in l1:
#         l1.append(i)
#     else:
#         print(i,end=' ')
# ------------by using Counter
# from collections import Counter
# li=[1, 3, 2, 6, 2, 3, 5, 6, 4, 5]
# d = Counter(li)
# print(d)
# repeated_list = list([num for num in d if d[num]>1])
# print("Duplicate integers: ",repeated_list)

# -----------------Cumulative Sum of list
# list1 = [10,20,30,40,50]
# new_list = []
# j = 0
# for i in range(0,len(list1)):
#     j = j + list1[i]
#     new_list.append(j)
# print(new_list)
# -------------------Sum of list digits in string
# test_list = [12, 67, 98, 34]
# print(test_list)
# res = []
# for each in test_list:
#     sum = 0
#     for digit in str(each):
#         sum = sum+int(digit)
#     res.append(sum)
# print(res)
#List Comprehension method
# res = list(map(lambda ele: sum(int(sub) for sub in str(ele)), test_list))
# --------------------------------create sublists of len n from list
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
# n = 4
# listofsubs = [l[i:i+n] for i in range(0,len(l),n)]
# print(listofsubs)
# ----------------------------------values of first list using second
# def sort_list(list1, list2):
#     zipped_pairs = zip(list2, list1)
#     z = [y for x,y in sorted(zipped_pairs)]
#     return z
# # driver code
# x = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
# y = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
 
# print(sort_list(x, y))

# ---------------------------------- add two matrix
# X = [[1,2,3],
#     [4 ,5,6],
#     [7 ,8,9]]
# Y = [[9,8,7],
#     [6,5,4],
#     [3,2,1]]
# result = [[0,0,0],
#         [0,0,0],
#         [0,0,0]]
# for i in range(len(X)):
#     for j in range(len(X[0])):
#         result[i][j] = X[i][j] + Y[i][j]
# for r in result:
#     print(r)
# -----------------------------------------multiply two matrices
# A = [[12, 7, 3],
#     [4, 5, 6],
#     [7, 8, 9]]
 
# # take a 3x4 matrix   
# B = [[5, 8, 1, 2],
#     [6, 7, 3, 0],
#     [4, 5, 9, 1]]
     
# result = [[0, 0, 0, 0],
#         [0, 0, 0, 0],
#         [0, 0, 0, 0]]
 
# # iterating by row of A
# for i in range(len(A)):
 
#     # iterating by column by B
#     for j in range(len(B[0])):
 
#         # iterating by rows of B
#         for k in range(len(B)):
#             result[i][j] += A[i][k] * B[k][j]
 
# for r in result:
#     print(r)
# -----------------------------------
