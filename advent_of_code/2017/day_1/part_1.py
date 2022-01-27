f = open("input.txt", "r")

nums = f.readlines()[0]
total = 0

for i in range(len(nums) - 1):
    if nums[i] == nums[i + 1]:
        total += int(nums[i])

if nums[-1] == nums[0]:
    total += int(nums[0])

print(total)
