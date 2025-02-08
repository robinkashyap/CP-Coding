def secondLar(arr):
    n = len(arr)
    max1 = float("-inf")
    max2 = float("-inf")
    max3 = float("-inf")
    for i in range(n):
        if arr[i]>max1:
            max3 = max2
            max2 = max1
            max1 = arr[i]
        elif arr[i]>max2 and arr[i]!=max1:
            max3 = max2
            max2 = arr[i]
        elif arr[i]>max3 and arr[i]!=max3:
            max3 = arr[i]
    return max3

arr = [800,100,300,0,500,900,1000]
print(secondLar(arr))