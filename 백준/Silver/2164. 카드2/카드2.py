from collections import deque

n = int(input())
nums = deque(range(1, n + 1))

for i in range(n - 1):
    nums.popleft()
    nums.append(nums[0])
    nums.popleft()

print(nums[0])