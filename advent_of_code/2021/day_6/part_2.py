from collections import Counter

f = open("input.txt", "r")
lantern_fish = f.readlines()[0].split(",")

c = Counter(lantern_fish)

key_dict = {"0", "1", "2", "3", "4", "5", "6", "7", "8"}
for i in range(256):
    keys = c.keys()
    new_lantern_fish = dict([(key, 0) for key in key_dict])
    for key in keys:
        if (int(key) - 1) < 0:
            new_lantern_fish["6"] += c[key]
            new_lantern_fish["8"] += c[key]
        else:
            new_lantern_fish[str(int(key) - 1)] += c[key]
    c = new_lantern_fish

total = 0
for key in c:
    total += c[key]
print(total)
