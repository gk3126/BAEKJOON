a = int(input())
nums = []

for i in range(a):
    n = int(input())
    nums.append(n)

nums.sort()

for num in nums:
    print(num)