f = open("input.txt", "r")

directions = f.readlines()[0]
# initialize empty grid with zeros
matrix = [[0] * 1000 for _ in range(1000)]
i = 500
j = 500
matrix[i][j] += 1

for dir in directions:
    if dir == "^":
        j += 1
    elif dir == ">":
        i += 1
    elif dir == "<":
        i -= 1
    else:
        j -= 1
    matrix[i][j] += 1

total = 0
for row in matrix:
    for cell in row:
        if cell >= 1:
            total += 1

print(total)
