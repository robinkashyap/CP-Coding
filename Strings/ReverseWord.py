# Time Complexity - O(n)
# Space Complexity - O(n)

# Reverse the words 

# My name is Robin   ---->   Robin is name My

def reverseWord(arr,start,end):
        while(start<=end):
            arr[start], arr[end] = arr[end], arr[start]
            start = start + 1
            end = end - 1 

def reverseString(str):
    arr = list(str)
    n = len(arr)
    j = n-1
    i = 0
    l = 0

    for i in range(n):
        if arr[i] == ' ':
            reverseWord(arr,l,i-1)
            l = i + 1
            
    reverseWord(arr,l,n-1)

    return ''.join(arr)

str = 'My Name is Robin'
result = reverseString(str)
print(result)