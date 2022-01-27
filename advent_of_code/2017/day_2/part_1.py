f = open("input.txt", "r")
nums = f.readlines()
checksum = 0

for i in range(len(nums)):
    row = [int(x) for x in nums[i].replace("\t", " ").split(" ")]
    checksum += max(row) - min(row)

print(checksum)
