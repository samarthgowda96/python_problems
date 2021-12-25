from os import nice


f = open("input.txt", "r")

strs = f.readlines()
vowels = ["a", "e", "i", "o", "u"]
nice_strings_count = 0

for string in strs:
    double_letters_satisfied = False
    contains_invalid_strings = False
    vowel_count = 0
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            double_letters_satisfied = True

        if string[i] + string[i + 1] == "ab":
            contains_invalid_strings = True
        elif string[i] + string[i + 1] == "cd":
            contains_invalid_strings = True
        elif string[i] + string[i + 1] == "pq":
            contains_invalid_strings = True
        elif string[i] + string[i + 1] == "xy":
            contains_invalid_strings = True

        if string[i] in vowels:
            vowel_count += 1

        if contains_invalid_strings:
            break
    if string[-1] in vowels:
        vowel_count += 1

    if vowel_count >= 3 and not contains_invalid_strings and double_letters_satisfied:
        nice_strings_count += 1

print(nice_strings_count)
