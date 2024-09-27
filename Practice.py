def largest(arr):
    n = len(arr)
    first_largest, second_largest = -1000000, -1000000
    for i in range(n):
        if arr[i]>first_largest:
            second_largest = first_largest
            first_largest = arr[i]
    return second_largest

arr = [100, -1, 2, -3, 1, 50]
print(largest(arr))