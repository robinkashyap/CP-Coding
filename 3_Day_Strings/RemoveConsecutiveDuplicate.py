# Time complexity - O(n^2) due to pop operation as it is also shifting all the elements to left
# Space complexity - O(n)

# For a given string(str), remove all the consecutive duplicate characters.


# def removeConsDup(str):
#     arr = list(str)
#     n = len(arr)
#     i = 0
#     while(i<n-1):
#         if arr[i]==arr[i+1]:
#             arr.pop(i)
#             n = n - 1
#         else:
#             i = i + 1
#     return ''.join(arr)


# To reduce time complexity we can append the array

# Time Complexity - O(n)
# Space Complexity - O(n)


def removeConsDup(str):
    arr=[]
    for i in range(0, len(str)-1):
        if str[i] != str[i+1]:
            arr.append(str[i+1])
    return ''.join(arr)



str = 'aaabccbcdbdd'
result = removeConsDup(str)
print(result)