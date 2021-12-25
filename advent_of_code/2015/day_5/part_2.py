from os import nice


f = open("input.txt", "r")

strs = f.readlines()
nice_strings_count = 0

for string in strs:
    pair_satisfied = False
    repeated_letter = False
    for i in range(len(string) - 2):
        if string[i] + string[i + 1] in string[i + 2 :]:
            pair_satisfied = True

        if string[i] == string[i + 2]:
            repeated_letter = True

    if pair_satisfied and repeated_letter:
        nice_strings_count += 1

print(nice_strings_count)
