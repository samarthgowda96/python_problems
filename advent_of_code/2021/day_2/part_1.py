f = open("input.txt", "r")

lines = f.readlines()

horizontal_position = 0
depth = 0

for line in lines:
    dir, num = line.split()
    num = int(num)

    if "forward" in line:
        horizontal_position += num
    elif "down" in line:
        depth += num
    elif "up" in line:
        depth -= num

print(horizontal_position * depth)
