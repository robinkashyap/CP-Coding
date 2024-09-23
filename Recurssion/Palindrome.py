def isPalindrome(string):
    n = len(string)
    if  n == 0 or n ==1:
        return True
    if string[0] == string[n-1]:
        return isPalindrome(string[1:n-1])
    else:
        return False



s = input()
result = isPalindrome(s)
print(result)
