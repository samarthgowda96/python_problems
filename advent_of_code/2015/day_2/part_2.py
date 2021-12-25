f = open("input.txt", "r")

lines = f.readlines()
total = 0

for i in range(len(lines)):
    l, w, h = [int(x) for x in lines[i].split("x")]
    total += min(2 * l + 2 * w, 2 * w + 2 * h, 2 * l + 2 * h) + l * w * h

print(total)
