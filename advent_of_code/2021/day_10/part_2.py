f = open("input.txt", "r")
lines = [x.strip("\n") for x in f.readlines()]

opening_brackets = ["(", "[", "{", "<"]
closing_brackets = [")", "]", "}", ">"]

totals = []

for line in lines:
    total = 0
    my_stack = []
    corrupted = False
    for char in line:
        if char in opening_brackets:
            my_stack.append(opening_brackets.index(char))
        else:
            if closing_brackets.index(char) == my_stack[-1]:
                my_stack.pop()
            else:
                corrupted = True
                break
    if not corrupted:
        while my_stack:
            char = my_stack.pop()
            total *= 5
            total += char + 1

        totals.append(total)

print(sorted(totals)[int(len(totals) / 2)])
