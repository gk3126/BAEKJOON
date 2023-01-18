num = int(input())
a = input()

nums = []
for i in range(num):
    code = ord(a[i]) - 96
    nums.append(code)
    
answer = 0
for i in range(num):
    answer += nums[i] * 31 ** i

print(answer % 1234567891)