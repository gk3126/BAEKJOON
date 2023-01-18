c = int(input())

for i in range(c):
    nums = list(map(int,input().split()))
    avg = sum(nums[1:]) / nums[0]
    cnt = 0
    for num in nums[1:]:
        if avg < num:
            cnt += 1
    answer = cnt / nums[0] * 100
    print(f'{answer:.3f}%')