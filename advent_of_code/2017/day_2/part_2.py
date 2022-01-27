from audioop import reverse


f = open("input.txt", "r")
nums = f.readlines()
checksum = 0

for i in range(len(nums)):
    row = [int(x) for x in nums[i].replace("\t", " ").split(" ")]
    row.sort(reverse=True)

    for j in range(len(row)):
        for num in row[j + 1 :]:
            if row[j] % num == 0:
                checksum += int(row[j] / num)
                break

print(checksum)
