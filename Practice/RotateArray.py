def rotateLeft(arr,d):
    n = len(arr)
    d = d%n
    temp = [0]*d
    for i in range(d):
        temp[i] = arr[i]  #[1,2,3,4]
    for j in range(n-d):
        arr[j] = arr[j+d] 
    for k in range(n-d,n):
        arr[k]=temp[k-(n-d)]
    return arr
    
def rotateRight(arr,d):  #[4,5,6,7,1,2,3]
    n = len(arr)
    d = d%n
    temp = [0]*d
    for i in range(n-d,n):
        temp[i-(n-d)] = arr[i]
    for j in range(n - d - 1, -1, -1):  
        arr[j + d] = arr[j] 
    for k in range(d):
        arr[k]=temp[k]
    return arr


 

arr = [1,2,3,4,5,6,7]
d = 4
print(rotateLeft(arr,d))
print(rotateRight(arr,d))
