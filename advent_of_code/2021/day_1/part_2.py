f = open("input.txt", "r")

nums = f.readlines()
nums = [int(i) for i in nums]

count = 0

sum_sliding_windows = []

for i in range(len(nums) - 2):
    sum_sliding_windows.append(nums[i] + nums[i + 1] + nums[i + 2])

print(sum_sliding_windows)

for i in range(1, len(sum_sliding_windows)):
    if sum_sliding_windows[i - 1] < sum_sliding_windows[i]:
        count += 1

print(count)
