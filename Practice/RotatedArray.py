def reverse(arr,start,end):
    while(start<end):
        arr[start],arr[end] = arr[end],arr[start]
        start+=1
        end-=1

def rotateLeft(arr,d):
    n = len(arr)
    d = d%n
    reverse(arr,d,n-1)
    reverse(arr,0,d-1)
    reverse(arr,0,n-1)
    return arr

def rotateRight(arr1,d):
    n = len(arr1)
    d = d%n
    reverse(arr1,0,n-1)
    reverse(arr1,0,d-1)
    reverse(arr1,d,n-1)
    return arr1


arr = [1,2,3,4,5,6,7]
arr1 = [1,2,3,4,5,6,7]
d = 4
print(rotateLeft(arr,d))
print(rotateRight(arr1,d))