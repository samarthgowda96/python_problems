#!/usr/bin/env python3

def titlecase(title, exceptions):
    words = title.split(" ")
    formatted_title = []
    for word in words:
        if word.lower() in exceptions:
            formatted_title.append(word.lower())
        else:
            formatted_title.append(word.capitalize())
    return " ".join(formatted_title)


if __name__ == "__main__":
    #test cases
    print(titlecase("byte academy is the best", "is, the"))
    exceptions = ["jumps", "the", "over"]
    print(titlecase("the quick brown fox jumps over the lazy dog", exceptions))
    exceptions = ["are", "is", "in", "your", "my"]
    print(titlecase("THE vitamins ARE IN my fresh CALIFORNIA raisins", exceptions))
