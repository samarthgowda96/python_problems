f = open("input.txt", "r")

matrix = [list(x) for x in f.readlines()]
new_matrix = []
for line in matrix:
    new_matrix.append([int(x) for x in line if x != "\n"])

matrix = new_matrix
total = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        low_point = True

        if j >= 1:  # check left
            if matrix[i][j - 1] > matrix[i][j]:
                low_point = low_point and True
            else:
                low_point = False

        if j < len(matrix[i]) - 1:  # check right
            if matrix[i][j + 1] > matrix[i][j]:
                low_point = low_point and True
            else:
                low_point = False

        if i >= 1:  # check up
            if matrix[i - 1][j] > matrix[i][j]:
                low_point = low_point and True
            else:
                low_point = False

        if i < len(matrix) - 1:  # check down
            if matrix[i + 1][j] > matrix[i][j]:
                low_point = low_point and True
            else:
                low_point = False

        if low_point == True:
            total += 1 + matrix[i][j]

print(total)
