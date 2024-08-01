

def replaceChar(str, ch1, ch2):
    n = len(str)
    str_new = ""
    for i in range(n):
        if str[i] == ch1:
            str_new = str_new + ch2
        else:
            str_new = str_new + str[i]
    return str_new

str = "Malayalam"
ch1 = 'a'
ch2 = "*"
result = replaceChar(str, ch1, ch2)
print(result)