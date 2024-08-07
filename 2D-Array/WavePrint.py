# Time Complexity - O(row*col)
# Space Complexity - O(1)

# For a given two-dimensional integer array/list of size (N x M), 
# print the array/list in a sine wave order, i.e, print the first column top to bottom, next column bottom to top and so on.

# [[1,2,3,4],[5,6,7,8],[9,10,11,12]]  -->  1 5 9 10 6 2 3 7 11 12 8 4 


def wavePrint(mat, row, col):
    for i in range(col):
        if i%2 == 0:
            j = 0
            while j <= row - 1:
                print(mat[j][i], end =" ")
                j += 1
        else:
            j = row - 1
            while j>=0:
                print(mat[j][i], end =" ")
                j -= 1

            

mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
wavePrint(mat,3,4)