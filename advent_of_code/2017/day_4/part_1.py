f = open("input.txt", "r")
passphrases = f.readlines()

valid_phrases = 0

for phrase in passphrases:
    phrase = phrase.split()

    if sorted(phrase) == sorted(list(set(phrase))):
        valid_phrases += 1

print(valid_phrases)
