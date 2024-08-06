
def largeSumColumnRow(list, row, col):
    max_col_sum, max_row_sum = 0, 0
    col_index, row_index = -1, -1
    # Column Sum
    for j in range(col):
        col_sum = 0
        for i in range(row):
            col_sum += list[i][j]
        if max_col_sum < col_sum:
            max_col_sum = col_sum
            col_index = j
    # Row Sum
    for i in range(row):
        row_sum = 0
        for j in range(col):
            row_sum += list[i][j]
        if max_row_sum < row_sum:
            max_row_sum = row_sum
            row_index = i
    
    if max_row_sum >= max_col_sum:
        print(f'Row {row_index} have the maximum sum of {max_row_sum}')
    else:
        print(f'Column {col_index} have the maximum sum of {max_col_sum}')
    
list = [[6, 9, 8, 8],
        [9, 2, 4, 1],
        [8, 3, 9, 3],
        [8, 7, 8, 6]
       ] 

largeSumColumnRow(list, 4,4)