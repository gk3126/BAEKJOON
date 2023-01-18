n = int(input())
nums = list(range(1, n + 1))
answer = []

for i in range(n - 1):
    answer.append(nums[0])
    del nums[0]
    nums.append(nums[0])
    del nums[0]

answer.append(nums[0])

print(*answer)