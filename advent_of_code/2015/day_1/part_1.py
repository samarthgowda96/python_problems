f = open("input.txt", "r")

count = 0
directions = f.readlines()[0]

for char in directions:
    if char == "(":
        count += 1
    else:
        count -= 1

print(count)
