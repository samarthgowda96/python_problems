f = open("input.txt", "r")

pos = [int(x) for x in f.readlines()[0].split(",")]
pos_set = list(set(pos))

fuel_possibilities = []

for i in range(max(pos_set)):
    fuel = 0
    for position in pos:
        if position != i:
            fuel += abs(position - i)
    fuel_possibilities.append(fuel)

print(min(fuel_possibilities))
