# Time Complexity - O(n)
# Space Complexity - O(n)

# Reverse each word present in the string

# My Name is Robin  ------>   yM emaN si niboR


def reverseEachWord(str):
    arr = list(str)
    n = len(arr)
    j = 0
    def reverseWord(arr,start,end):
        while(start<=end):
            arr[start], arr[end] = arr[end], arr[start]
            start = start + 1
            end = end - 1
    for i in range(n):
        if arr[i] == ' ':
            reverseWord(arr,j,i-1)
            j = i + 1
    reverseWord(arr,j,n-1)
    return ''.join(arr)


str = 'My Name is Robin'
result = reverseEachWord(str)
print(result)