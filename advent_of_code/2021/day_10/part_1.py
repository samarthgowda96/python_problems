f = open("input.txt", "r")
lines = [x.strip("\n") for x in f.readlines()]

opening_brackets = ["(", "[", "{", "<"]
closing_brackets = [")", "]", "}", ">"]

my_stack = []
total = 0

for line in lines:
    for char in line:
        if char in opening_brackets:
            my_stack.append(opening_brackets.index(char))
        else:
            closing_brackets_index = closing_brackets.index(char)
            if closing_brackets_index == my_stack[-1]:
                my_stack.pop()
            else:
                if closing_brackets_index == 0:
                    total += 3
                elif closing_brackets_index == 1:
                    total += 57
                elif closing_brackets_index == 2:
                    total += 1197
                else:
                    total += 25137
                break

print(total)
