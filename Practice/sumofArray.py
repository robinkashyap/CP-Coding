def sumArray(arr1,arr2):
    m = len(arr1) - 1
    n = len(arr2) - 1
    k = max(m,n) + 1
    arr = [0]*(k+1)
    carry = 0
    while(m>=0 and n>=0):
        sum = arr1[m] + arr2[n] + carry
        arr[k] = sum%10
        carry = sum//10
        m-=1
        n-=1
        k-=1
    while(m>=0):
        sum = arr1[m] + carry
        arr[k] = sum%10
        carry = sum//10
        m-=1
        k-=1
    while(n>=0):
        sum = arr2[n] + carry
        arr[k] = sum%10
        carry = sum//10
        n-=1
        k-=1
    if carry > 0:
        arr[0] = carry
    else:
        arr = arr[1:]
    return arr


arr1 = [6,9,9,9]
arr2 = [9,9,9,9]
print(sumArray(arr1,arr2))