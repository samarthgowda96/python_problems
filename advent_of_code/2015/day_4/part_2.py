import hashlib

f = open("input.txt", "r")

secret_key = f.readlines()[0]
hash = ""
i = 1

while hash[:6] != "000000":
    i += 1
    hash = hashlib.md5(f"{secret_key}{i}".encode()).hexdigest()

print(i)
