def secondSmallest(arr):
    first_largest = float('-inf')
    second_largest = float('-inf')
    third_largest = float('-inf')
    for i in range(len(arr)):
        if arr[i] > first_largest:
            second_largest = first_largest
            third_largest = second_largest
            first_largest = arr[i]
        elif arr[i]>second_largest and arr[i]<first_largest:
            second_largest = third_largest
            second_largest = arr[i]
        elif arr[i]>third_largest and arr[i]<second_largest:
            third_largest = arr[i]
    return third_largest

arr = [1,5,5,5,5,4]
print(secondSmallest(arr))