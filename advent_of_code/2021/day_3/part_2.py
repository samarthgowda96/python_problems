f = open("input.txt", "r")
nums = f.readlines()

oxygen_numbers = nums
i = 0
while len(oxygen_numbers) > 1:
    count = 0
    for num in oxygen_numbers:
        if num[i] == "0":
            count += 1
    most_common_bit = "0" if (count > (len(oxygen_numbers) / 2)) else "1"
    oxygen_numbers = [x for x in oxygen_numbers if x[i] == most_common_bit]
    i += 1

scrubber_numbers = nums
i = 0
while len(scrubber_numbers) > 1:
    count = 0
    for num in scrubber_numbers:
        if num[i] == "0":
            count += 1
    least_common_bit = "0" if (count <= (len(scrubber_numbers) / 2)) else "1"
    scrubber_numbers = [x for x in scrubber_numbers if x[i] == least_common_bit]
    i += 1

print(
    int(oxygen_numbers[0].replace("\n", ""), 2)
    * int(scrubber_numbers[0].replace("\n", ""), 2)
)
