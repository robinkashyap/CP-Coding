# Time Complexity - O(row*col)
# Space Complexity - O(1)

# Find the sum of largest column in 2D Array


def largeSumColumn(list, row, col):
    column = -1
    out = 0
    for j in range(col):
        sum = 0
        for i in range(row):
            sum += list[i][j]
        # for ele in list:
        #     sum += ele[j]
        if out < sum:
            out = sum
            column = j
    return out, column

list = [[9,2,9,6],
        [5,9,8,9],
        [9,9,9,9]]
row = 3
col = 4
sum,column = largeSumColumn(list, row, col)
print(sum,column, end =" ")
        

        
