import sys

n = int(sys.stdin.readline())
nums = [0] * 10001

for i in range(n):
    num = int(sys.stdin.readline())
    nums[num] += 1
    
for i in range(1,10001):
    for j in range(nums[i]):
        print(i)