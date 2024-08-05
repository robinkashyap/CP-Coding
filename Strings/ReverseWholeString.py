# Time Complexity - O(n)
# Space Complexity - O(n)

# Reverse the whole string

# My name is Robin   ------>   niboR si emaN yM


def reverseString(str):
    arr = list(str)
    n = len(arr)
    j = n-1
    i = 0

    while(i<=j):
        arr[i], arr[j] = arr[j], arr[i]
        i = i + 1
        j = j-1
    return ''.join(arr)

str = 'My Name is Robin'
result = reverseString(str)
print(result)




