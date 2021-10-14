# Palindrome?
# def isPalindrome(strin):
#     return strin == strin[::-1]
# print(isPalindrome(input("Print String:")))
# ----------------------------is symmetrical
# mystr = "lolwalol"
# half = int(len(mystr)/2)
# if len(mystr)%2 == 0:
#     first_half = mystr[0:half]
#     sec_half = mystr[half:]
# else:
#     first_half = mystr[:half]
#     sec_half = mystr[half+1:]

# if first_half == sec_half: print("Symmetrical")
# else: print("Assymetrical")
# --------------------------------- Reverse a sentence
# def reverseit(sent):
#     revsent = sent.split(' ')
#     revsent = ' '.join(reversed(revsent))
#     return revsent
# print(reverseit(input("Enter sentence: ")))
# --------------------------------- Remove ith character from a string
# teststr = "vstromisthebest"
# print(teststr)
# new_str = teststr.replace('s','')
# print(new_str)
# new_str = teststr.replace('s','',1) # for the first occurance only
# print(new_str)
#----------------------------------- Check if substring is present in string
# stringwa = "pacito oacito male male ito"
# substr = "male"
# if substr in stringwa:  #method1
#     print("Eureka!")
# ------------ by Find
# def checkSubstr(stringwa, substr):
#     if stringwa.find(substr) == -1:
#         print("Nay")
#     else: print("yay!")
# checkSubstr(stringwa, substr)
# ----------------by RE
# import re
# if re.search(substr,stringwa):
#     print("milya")
# else: print("nahi milya")
# ---------------------------------------------Count frequency of word in sting
# teststr = "jo hua so hua"
# res = teststr.count("hua")
# print(res)
# ------------------------------Replace snake case to pascal case
# stringea = "nerds_are_for_dorks_geeks_are_forever"
# print(stringea.replace("_"," ").title().replace(" ", ""))
#---------------------------------------------Count num of matching char in string
# def contstr(str1, str2):
#     setstr1 = set(str1)
#     setstr2 = set(str2)
#     matched_chars = setstr1 and setstr2
#     print(matched_chars)

# str1 = "adfeiffhewf"
# str2 = "sskdfiaadwfkl"
# contstr(str1,str2)
# ----------------------------------------max frequency of a string
# from collections import Counter
# test_str = "GeeksforGeeks"
# print ("The original string is : " + test_str)
# res = Counter(test_str)
# res = max(res, key = res.get) 
# print ("The maximum of all characters in GeeksforGeeks is : " + str(res))
# ----------------------------------------- find special char in a string
# import re
# def specialchar(string1):
#     regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
#     if regex.search(string1) == None:
#         print("String is accepted")
#     else: print("String is not accepted")

# print(specialchar("this is some string"))
# -----------------------------------------find uncommon words in two lists
# str1 = "there is a snake here".split()
# str2 = "there are many mice here".split()
# mat = set(str2).symmetric_difference(set(str1))
# print(mat)
# ----------------------------------------- 
test_str = 'Gfg is best . Gfg also has Classes now. \
                Classes help understand better . '
print("The original string is : " + str(test_str))
repl_dict = {'Gfg' :  'It', 'Classes' : 'They' }
test_list = test_str.split(' ')
dup = set()
print(dict(enumerate(test_list)))
for index, ele in enumerate(test_list):
    if ele in repl_dict:
        if ele in dup:
            test_list[index] = repl_dict[ele]
        else: 
            dup.add(ele)
dup2 = ' '.join(test_list)
print(str(dup2))