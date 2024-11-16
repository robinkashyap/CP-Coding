def missingNumber(arr):
    n = len(arr) + 1
    sum_n = (n*(n+1))//2
    sum_a = 0
    for i in range(len(arr)):
        sum_a = sum_a + arr[i]
    return sum_n - sum_a
arr = [1,2,3,4,6,7,8,9,10]
print(missingNumber(arr))