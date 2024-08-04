def compressString(str):
    arr = [0]*26
    arr1 = []

    for i in str:
        i = i.lower()
        arr[ord(i)-97] += 1

    arr2 =[]
    
    for j in str:
        if j not in arr2:
            count = arr[ord(j)-97]
            arr1.append(j)
            if count>1:
                arr1.append(f'{count}')
            arr2.append(j)
    return ''.join(arr1)

str = 'xxccxddwcwda'
result = compressString(str)
print(result)