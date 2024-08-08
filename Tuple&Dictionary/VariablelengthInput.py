# Variable lenght input to a function for that we need to use *

def sum(a, b, *s):
    add = a + b
    for i in s:
        add = add + i
    return add

result = sum(1,2,3,4,5,6,7,8,9,10)
print(result)
