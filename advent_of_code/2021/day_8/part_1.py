f = open("input.txt", "r")
lines = [x.split(" | ")[1].strip("\n").split(" ") for x in f.readlines()]
count = 0
for line in lines:
    for string in line:
        if len(string) == 2 or len(string) == 3 or len(string) == 4 or len(string) == 7:
            count += 1
print(count)
