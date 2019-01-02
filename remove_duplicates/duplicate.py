#!/usr/bin/env python3

#remove all the consecutive duplicates and put them in a separate string
def remove_duplicate(string):
    #make lists that keep the unique and duplicate characters
    unique = []
    duplicates = []
    for char in string:
        if len(unique) == 0: #if the unique list is empty, append the first character
            unique.append(char)
        else: #if the unique list is not empty
            if unique[-1] == char: #if the previous character in unique is the current char
                duplicates.append(char)
            else: #prev character is different
                unique.append(char)

    #join the characters in each list
    ustring = "".join(unique) #unique string
    dstring = "".join(duplicates) #duplicate string

    #format the output
    print("("+ustring +","+ dstring+")")

if __name__ == "__main__":
    remove_duplicate("balloons")
    remove_duplicate("aabbccddeded")
    remove_duplicate("flabby aapples")
