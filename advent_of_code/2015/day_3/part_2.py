f = open("input.txt", "r")

directions = f.readlines()[0]
# initialize empty grid with zeros
matrix = [[0] * 1000 for _ in range(1000)]
i = 500
j = 500
robo_i = 500
robo_j = 500
matrix[i][j] += 2  # both Santa and robo-Santa visit

for idx in range(len(directions)):
    if idx % 2 == 0:
        if directions[idx] == "^":
            j += 1
        elif directions[idx] == ">":
            i += 1
        elif directions[idx] == "<":
            i -= 1
        else:
            j -= 1
        matrix[i][j] += 1
    else:
        if directions[idx] == "^":
            robo_j += 1
        elif directions[idx] == ">":
            robo_i += 1
        elif directions[idx] == "<":
            robo_i -= 1
        else:
            robo_j -= 1
        matrix[robo_i][robo_j] += 1

total = 0
for row in matrix:
    for cell in row:
        if cell >= 1:
            total += 1

print(total)
