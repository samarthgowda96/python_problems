f = open("input.txt", "r")
lines = [x.split(" | ")[1].strip("\n").split(" ") for x in f.readlines()]
print(lines)
total = 0

for line in lines:
    output = ""
    for string in line:
        sorted_string = sorted(list(string))
        if sorted_string == ["a", "b", "c", "d", "e", "g"]:
            output += "0"
        elif sorted_string == ["a", "b"]:
            output += "1"
        elif sorted_string == ["a", "c", "d", "f", "g"]:
            output += "2"
        elif sorted_string == ["a", "b", "c", "d", "f"]:
            output += "3"
        elif sorted_string == ["a", "b", "e", "f"]:
            output += "4"
        elif sorted_string == ["b", "c", "d", "e", "f"]:
            output += "5"
        elif sorted_string == ["b", "c", "d", "e", "f", "g"]:
            output += "6"
        elif sorted_string == ["a", "b", "d"]:
            output += "7"
        elif sorted_string == ["a", "b", "c", "d", "e", "f", "g"]:
            output += "8"
    # total += int(output)
    print(output)
print(total)
