# Time Complexity - O(n^2)
# Space Complexity - O(n)

# Here we count each char occurence and write their sum with them

# 'aasadfssxxxx'  --->  'a3s3dfx4'


def compressString(str):
    n = len(str)
    arr = [0]*26
    arr1 = []
    arr2 = []
    count = 0

    for i in str:
        i = i.lower()
        arr[ord(i)-97] += 1
    
    for j in str:
        if j not in arr2:
            arr1.append(j)
            if arr[ord(j)-97]>1:
                arr1.append(f'{arr[ord(j)-97]}')
        arr2.append(j)
    return ''.join(arr1)
str = 'aasadfssxxxx'
result = compressString(str)
print(result)