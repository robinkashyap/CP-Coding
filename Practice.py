def largest(arr):
    n = len(arr)
    largest = -1000000
    for i in range(n):
        if arr[i]>largest:
            largest = arr[i]
    return largest

arr = [0, -1, 2, -3, 1, 50, 100, 100]
print(largest(arr))