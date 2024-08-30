
def checkRedundantBrackets(a):
    li = []
    for ele in a:
        if ele == ")":
            top_element = top(li)
            li.pop()
            flag = True
            while(len(li)!=0 and top_element!='('):
                if (top_element == '+' or top_element == '-' or top_element == '*' or top_element == '/'):
                    flag = False
                top_element = top(li)
                li.pop()
            if flag == True:
                return True
        else:
            li.append(ele)
    return False

def top(li):
    return li[len(li) - 1]


a = '(a+)'
result = checkRedundantBrackets(a)
print(result)

