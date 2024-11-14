def reverse(arr,start,end):
    while(start<end):
        arr[start],arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def leftshift(arr,k):
    n = len(arr)
    k = k%n
    reverse(arr,0,k-1)
    reverse(arr,k,n-1)
    reverse(arr,0,n-1)
    return arr

def rightshift(arr,k):
    n = len(arr)
    k = k%n
    reverse(arr,n-k,n-1)
    reverse(arr,0,n-k-1)
    reverse(arr,0,n-1)
    return arr

arr1 = [1,2,3,4,5,6,7]
arr2 = [1,2,3,4,5,6,7]


k = 4
print(leftshift(arr1,k))    # [5,6,7,1,2,3,4]
print(rightshift(arr2,k))   # [4,5,6,7,1,2,3]