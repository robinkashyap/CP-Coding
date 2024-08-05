# Time Complexity - O(n^2)
# Space Complexity - O(1)

# Given an array A[] of n numbers and another number x, the task is to check \n
# whether or not there exist two elements in A[] whose sum is exactly x. 

# in the below code you can also check how many pairs are present


def pairSum(arr,x):
    n = len(arr)
    count = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i] + arr[j] == x:
                count = count + 1
    return count

arr = [0, -1, 2, -3, 1]
x = 10
result = pairSum(arr,x)
if result != 0:
    print(f"{result} pair is present in the array")
else:
    print("Pair is not present in the array")