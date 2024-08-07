# Time Complexity - O(row*col)
# Space Complexity - O(row*col)


def spiralPrint(mat, row, col):
    left, right = 0, col - 1
    top, bottom = 0, row - 1

    arr = []
    while(left <= right and top <= bottom):
        for i in range(left, right + 1):
            arr.append(mat[top][i])
        top += 1

        for j in range(top, bottom + 1):
            arr.append(mat[j][right]) 
        right -= 1

        if top <= bottom:
            for k in range(right, left - 1 , -1):
                arr.append(mat[bottom][k])
            bottom -= 1
        if left <= right:
            for l in range(bottom, top - 1, -1):
                arr.append(mat[l][left])
            left += 1

    return arr

mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
result = spiralPrint(mat,4,4)
print(result)