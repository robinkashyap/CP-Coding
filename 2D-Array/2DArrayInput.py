# How to take input of 2D list from user
# i*col + j - formula two add elements at their position

str = input().split()
row,col = int(str[0]), int(str[1])
b = input().split()
list = [[int(b[i*col + j])for j in range(col)]for i in range(row)]
print(list)
