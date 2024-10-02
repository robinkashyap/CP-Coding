def compressStr(str):
    n = len(str)
    start = 0
    end = 0
    str1 = ''
    while(start<n):
        while(end<n and str[start]==str[end]):
            end += 1
        count = end - start
        str1 = str1 + str[start]
        if count>1:
            str1 = str1 + f'{count}'
        start = end
    return str1


str = 'aasadfssxxxx'
result = compressStr(str)
print(result)
