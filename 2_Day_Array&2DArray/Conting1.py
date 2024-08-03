# Time Complexity - O(n)
# Space Complexity - O(1)

# counting the maximum consecutive 1's

def counting1(arr):
    n = len(arr)
    max = 0
    count = 0
    for i in range(n):
        if arr[i] == 1:
            count = count + 1
        else:
            count = 0
        if max < count:
            max = count
    return max

arr = [1, 0, 1, 1, 1, 5, 1, 1, 1, 0, 1, 1]
result = counting1(arr)
print(result)
        
                   

