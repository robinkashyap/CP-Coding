# Time Complexity = O(n)
# Space Complexity = O(n)

# Here we count continuos char occurence and write their sum with them
# 'aasadfssxxxx' -->  'a2sadfs2x4'


def compressStr(str):
    n = len(str)
    start = 0
    end = 0
    str1 = ''
    while(start<n):
        while((end < n) and (str[end]==str[start])):
            end += 1
        count = end - start
        str1 = str1 + (str[start])
        if count>1:
            str1 = str1 + f'{count}'
        start = end
    return str1

str = 'aasadfssxxxx'
result = compressStr(str)
print(result)
