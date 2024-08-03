# Time Complexity - O(n)
# Space Complexity - O(1)

# counting the maximum consecutive 1's

def counting1(arr):
    n = len(arr)
    max_count = 0
    count = 0
    start_index = -1
    end_index = -1
    current_start = 0

    for i in range(n):
        if arr[i] == 1:
            count += 1
            if count == 1:
                current_start = i
        else:
            if count > max_count:
                max_count = count
                start_index = current_start
                end_index = i - 1
            count = 0

    # Check one last time in case the array ends with the longest sequence of 1s
    if count > max_count:
        max_count = count
        start_index = current_start
        end_index = n - 1

    return max_count, start_index, end_index


arr = [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
max, start, end = counting1(arr)
print(f"max 1's are {max} and starting from {start} to {end}")
        
                   

