# Time Complexity - O(max(m,n))
# Space Complexity - O(max(m,n))

# add the two array in third array 


def sumArray(arr1, arr2):
    n = len(arr1) - 1
    m = len(arr2) - 1
    k = max(n,m) + 1
    arr = [0]*(k + 1)
    carry = 0
    while (n>=0 and m>=0):
        sum = arr1[n] + arr2[m] + carry
        arr[k] = sum%10
        carry = sum//10
        n = n - 1
        m = m - 1
        k = k - 1
    while(n>=0):
        sum = arr1[n] + carry
        arr[k] = sum%10
        carry = sum//10
        n = n - 1
        k = k - 1        
    while(m>=0):
        sum = arr2[m] + carry
        arr[k] = sum%10
        carry = sum//10
        m = m - 1
        k = k - 1
    arr[0] = carry
    return arr

arr1 = [6, 9, 9, 9]
arr2 = [1, 2, 3]
result = sumArray(arr1, arr2)
print(result)