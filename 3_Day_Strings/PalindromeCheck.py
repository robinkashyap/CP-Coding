# Time Complexity - O(n)
# Space Complexity - O(1)

# Check the given string is Palindrome or not


def palindrome(str):
    n = len(str)
    i = 0
    j = n-1
    while (i<j):
        if str[i]==str[j]:
            i = i + 1
            j = j - 1
        else:
            return False
    return True

str = 'ab'
result = palindrome(str)
print(result)