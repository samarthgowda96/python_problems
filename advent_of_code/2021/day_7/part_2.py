f = open("input.txt", "r")

pos = [int(x) for x in f.readlines()[0].split(",")]
pos_set = list(set(pos))

fuel_possibilities = []
output = None
for i in range(max(pos_set)):
    fuel = 0
    for position in pos:
        if position != i:
            cost = 1
            while position != i:
                fuel += cost
                cost += 1
                position += 1 if position < i else -1
    fuel_possibilities.append(fuel)
    if fuel_possibilities and len(fuel_possibilities) >= 2:
        if fuel_possibilities[-2] < fuel_possibilities[-1]:
            output = fuel_possibilities[-2]
            break
    if output:
        break
print(output)
