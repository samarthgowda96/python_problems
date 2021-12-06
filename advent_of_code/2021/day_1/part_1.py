f = open("input.txt", "r")

nums = f.readlines()
nums = [int(i) for i in nums]

count = 0

for i in range(1, len(nums)):
    if nums[i - 1] < nums[i]:
        count += 1

print(count)
