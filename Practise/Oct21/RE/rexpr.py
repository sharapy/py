# import re
# def check(str,pattern):
#     if re.search(pattern, str):
#         print("Valid String")
#     else: print("Invalid String")

# # pattern = re.compile('^[1234]+$')
# pattern = r'^[1234]+$'
# check('421', pattern)
# check('12321231212',pattern)
# check('7654', pattern)
# ---------------------------find uppercase, lowercase, numerical, special char
# import re
# str1 = "This is g2g no 1, that's it !"
# uc_letter = re.findall(r'[A-Z]', str1)
# lc_letter = re.findall(r'[a-z]', str1)
# digits = re.findall(r'[0-9]', str1)
# sp_char = re.findall(r'[,!\']', str1)
# print(len(uc_letter)," ",len(lc_letter)," ", len(digits)," ", len(sp_char)," ")
#----------------------------find largest number from a string
import re
# def extract_max(str1):
#     nums = re.findall('\d+', str1)
#     nums = map(int,nums)
#     print(max(nums))
# str1 = input("Enter string: ")
# extract_max(str1)

# ---------------------------------matches URL in string
# str1 = "this is website http://wix.com and many more like https://needmorepractice.in not sure how many"
# url_pattern = r'http.*//\w*.?\w+.?\w{2,3}' #incorrect
# urls = re.findall(url_pattern, str1)
# print(urls)