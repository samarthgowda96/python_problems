f = open("input.txt", "r")
nums = f.readlines()
LENGTH_OF_NUMBERS = 12
counts = [0 for x in range(LENGTH_OF_NUMBERS)]
for num in nums:
    for i in range(len(num)):
        if num[i] == "0":
            counts[i] += 1

most_common_bits = []
for num in counts:
    if num > (len(nums) / 2):
        most_common_bits.append("0")
    else:
        most_common_bits.append("1")

least_common_bits = ["0" if x == "1" else "1" for x in most_common_bits]

gamma_rate = int("".join(most_common_bits), 2)
epsilon_rate = int("".join(least_common_bits), 2)

print(gamma_rate * epsilon_rate)
