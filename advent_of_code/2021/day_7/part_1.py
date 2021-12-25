from collections import Counter

f = open("input.txt", "r")

pos = [int(x) for x in f.readlines()[0].split(",")]

print(sum(pos) / len(pos))

c = Counter(pos)
majority_crabs_idx = 360


fuel = 0
for position in c:
    if position != majority_crabs_idx:
        fuel += abs(position - majority_crabs_idx) * c[position]
        # print(fuel, position, c[position])

# print(fuel)
