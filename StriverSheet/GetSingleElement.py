def get_single_element(arr):
    n = len(arr)
    xorr = 0
    for  i in range(n):
        xorr = xorr ^ arr[i]
    return xorr

arr = [1,1,2,3,2,4,5,5,3]
print(get_single_element(arr))