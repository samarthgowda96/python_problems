import numpy as np

f = open("input.txt", "r")
lantern_fish = [int(x) for x in f.readlines()[0].split(",")]

for i in range(80):
    new_fish = 0
    for i in range(len(lantern_fish)):
        lantern_fish[i] -= 1

    for i in range(len(lantern_fish)):
        if lantern_fish[i] == -1:
            lantern_fish[i] = 6
            new_fish += 1

    for i in range(new_fish):
        lantern_fish.append(8)

print(len(lantern_fish))
