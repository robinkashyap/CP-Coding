def compress(str):
    n = len(str)
    start,end,count = 0,0,0
    str1 = ''
    while(start<n):
        while((end<n) and (str[start] == str[end])):
            end+=1
        count = end - start
        str1 = str1 + str[start]
        if count > 1:
            str1 = str1 + f'{count}'
        start = end
    return str1

str = 'aasadfssxxxx'
result = compress(str)
print(result)
