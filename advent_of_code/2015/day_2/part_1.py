f = open("input.txt", "r")

lines = f.readlines()
total = 0

for i in range(len(lines)):
    l, w, h = [int(x) for x in lines[i].split("x")]
    total += 2 * l * w + 2 * w * h + 2 * h * l
    total += min(l * w, w * h, h * l)

print(total)
