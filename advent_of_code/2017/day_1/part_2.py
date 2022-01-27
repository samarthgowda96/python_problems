f = open("input.txt", "r")

nums = f.readlines()[0]
total = 0
middle = int(len(nums) / 2)

for i in range(middle):
    if nums[i] == nums[i + middle]:
        total += int(nums[i]) * 2

print(total)
