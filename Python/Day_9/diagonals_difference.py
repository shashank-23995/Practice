# my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print(my_matrix)
# print(len(my_matrix))
# for row in my_matrix:
#     for value in row:
#         print(row[value])

# for i in range(my_matrix)
#     # for j in range(len(i))
#     #     print(i,j)
#     print(i)

rows = int(input("Enter number of rows in matrix: "))
columns = int(input("Enter number of columns in matrix: "))
my_matrix = []
matrix_row = []
for i in range(0,rows):
    for j in range(0,columns):
            print("i = %d"% i)
            print("j = %d"% j)
            x = int(input("Enter values of matrix "))
            matrix_row[j] = x
        my_matrix[i] = matrix_row

print(my_matrix)           