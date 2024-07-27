# Time Complexity - O(2n)
# Space Complexity - O(1)


def reverse(arr,start,end):
    while(start<end):
        arr[start], arr[end] = arr[end], arr[start]
        start = start + 1
        end = end - 1

def arrayRotate(arr,d):
    n = len(arr)
    d = d%n
    reverse(arr,0,d-1)
    reverse(arr,d,n-1)
    reverse(arr,0,n-1)
    return arr

arr = [1, 2, 3, 4, 5, 6, 7]
d = 4
result = arrayRotate(arr,d)
print(result)
   