# Given a string S, compute recursively a new string where identical chars that are adjacent 
# in the original string are separated from each other by a "*".

# Constraints :
# 0 <= |S| <= 1000
# where |S| represents length of string S.

def pairStair(s):
    n = len(s)
    if n <= 1:
        return s
    if s[0] == s[1]:
        return s[0] + '*' + pairStair(s[1:])
    else:
        return s[0] + pairStair(s[1:])

print(pairStair("hello"))
print(pairStair("aaaa"))
