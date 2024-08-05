# Time Complexity - O(n)
# Space Complexity - O(1)


def linearSearch(arr,x):
    n=len(arr)
    for i in range(n):
        if arr[i] == x:
            return i
    return 0

arr = [10,3,4,76,23,55,89]
x = 4
result = linearSearch(arr,x)
if result == 0:
    print(f'{x} is not present inside the array')
else:
    print(f'{x} is present inside the array at position {result}')
