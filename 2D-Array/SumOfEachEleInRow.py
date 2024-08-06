# For a given two-dimensional integer array/list of size (N x M), 
# find and print the sum of each of the row elements in a single line, separated by a single space.

def rowElementSum(list,m,n):
    for i in range(m):
        sum = 0
        for j in range(n):
            sum = sum + list[i][j]
        print(sum, end=' ')

list = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
m = 3
n = 4
result = rowElementSum(list, m, n)
