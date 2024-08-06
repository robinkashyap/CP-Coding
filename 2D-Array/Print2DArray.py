# How to print 2D array having same col in each list

# list = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# row = 3
# col = 4
# for i in range(row):
#     for j in range(col):
#         print(list[i][j], end=" ")
#     print()

# How to print jagged list

list = [[1,2,3,4],[5,6],[7,8,9]]
for row in list:
    for ele in row:
        print(ele,end=" ")
    print()