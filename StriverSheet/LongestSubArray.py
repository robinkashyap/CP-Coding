def longestSubarray(arr,k):
    n = len(arr)
    length = 0
    p,q = -1, -1
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += arr[j]
            if sum == k:
                if length < j-i+1:
                    length = j-i+1
                    q = j
                    p = i

    return (p,q),length


a = [2, 3, 5, 1, 9]
k = 10
print(longestSubarray(a,k))
