import numpy as np

f = open("input.txt", "r")
lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip("\n").split(" -> ")

for i in range(len(lines)):
    lines[i] = [x.split(",") for x in lines[i]]

# initialize a blank grid with zeros
matrix = [[0] * 1000 for _ in range(1000)]
coordinates = []

for line in lines:
    x1 = int(line[0][0])
    y1 = int(line[0][1])

    x2 = int(line[1][0])
    y2 = int(line[1][1])

    if x1 == x2:
        y_coords = (
            [y for y in range(y1, y2 + 1)]
            if y1 < y2
            else [y for y in range(y2, y1 + 1)]
        )
        for y in y_coords:
            coordinates.append([x1, y])
    elif y1 == y2:
        x_coords = (
            [x for x in range(x1, x2 + 1)]
            if x1 < x2
            else [x for x in range(x2, x1 + 1)]
        )
        for x in x_coords:
            coordinates.append([x, y1])
    else:
        if abs(x2 - x1) == abs(y2 - y1):
            x_increasing = x1 < x2
            y_increasing = y1 < y2
            for i in range(abs(x2 - x1) + 1):
                if x_increasing:
                    x = x1 + i
                else:
                    x = x1 - i
                if y_increasing:
                    y = y1 + i
                else:
                    y = y1 - i
                coordinates.append([x, y])

for coord in coordinates:
    matrix[coord[0]][coord[1]] += 1

matrix = np.array(matrix)

print(np.count_nonzero(matrix >= 2))
