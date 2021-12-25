f = open("input.txt", "r")

count = 0
directions = f.readlines()[0]

for i in range(len(directions)):
    if directions[i] == "(":
        count += 1
    else:
        count -= 1
        if count == -1:
            print(i + 1)
            break
