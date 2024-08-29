import sys
def minDel(a):
    a_str = [0]*len(a)
    b_str = [0]*len(a)
 
    count_a, count_b = 0,0
    max_del = sys.maxsize
    for i in range(len(a)):
        if a[i] == 'a':
            count_a += 1
        a_str[i] = count_a
    for i in range(len(a)-1,0,-1):
        if a[i]=='b':
            count_b += 1
        b_str[i] = count_b
    for i in range(len(a)):
        sum = a_str[i] + b_str[i]
        diff = len(a) - sum
        if max_del > diff:
            max_del = diff
    return max_del

a = 'bbaaaaabb'
print(minDel(a))

