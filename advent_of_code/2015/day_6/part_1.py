f = open("input.txt", "r")
instructions = f.readlines()

matrix = [[0] * 1000 for _ in range(1000)]

for instruction in instructions:
    turn_on = False
    toggle = False
    turn_off = False
    if "turn on" in instruction:
        turn_on = True
    elif "toggle" in instruction:
        toggle = True
    elif "turn off" in instruction:
        turn_off = True
    instruction = (
        instruction.replace("turn on ", "")
        .replace("toggle ", "")
        .replace("turn off ", "")
        .strip("\n")
        .split(" through ")
    )
    first_coord = [int(x) for x in instruction[0].split(",")]
    second_coord = [int(x) for x in instruction[1].split(",")]

    for i in range(first_coord[0], second_coord[0] + 1):
        for j in range(first_coord[1], second_coord[1] + 1):
            if turn_on:
                matrix[i][j] = 1
            elif toggle:
                if matrix[i][j] == 0:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = 0
            else:
                matrix[i][j] = 0

total = 0
for row in matrix:
    for cell in row:
        if cell == 1:
            total += 1

print(total)
