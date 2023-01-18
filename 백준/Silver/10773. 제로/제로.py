import sys
input = sys.stdin.readline

k = int(input())
nums = []

for i in range(k):
    n = int(input())
    if n != 0:
        nums.append(n)
    else:
        nums.pop()

answer = sum(nums)
print(answer)