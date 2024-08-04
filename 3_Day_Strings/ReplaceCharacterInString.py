# Time Complexity - O(n^2) 
# In Python, string concatenation inside a loop is an 𝑂(𝑘) operation where 𝑘 is the current length of str_new. 
# This is because Python strings are immutable, so each concatenation creates a new string. 

# Space Complexity - O(n)

# Replace character in the string 


# def replaceChar(str, ch1, ch2):
#     n = len(str)
#     str_new = ""
#     for i in range(n):
#         if str[i] == ch1:
#             str_new = str_new + ch2
#         else:
#             str_new = str_new + str[i]
#     return str_new


# To reduce the time complexity we can change the string to list and after operations again changes to string

# Time Complexity - O(n)
# Sapce Complexity - O(n)


def replaceChar(str, ch1, ch2):
    str_list = list(str)
    for i in range(len(str_list)):
        if str_list[i] == ch1:
            str_list[i] = ch2
    return ''.join(str_list)


str = "Malayalam"
ch1 = 'a'
ch2 = "*"
result = replaceChar(str, ch1, ch2)
print(result)