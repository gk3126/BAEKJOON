n = int(input())
nums = list(map(int,input().split()))
m = int(input())
mnums = list(map(int,input().split()))

nums.sort()
for mnum in mnums:
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == mnum:
            print("1")
            break
        elif nums[mid] < mnum:
            left = mid + 1
        elif nums[mid] > mnum:
            right = mid - 1
    if left > right:
        print("0")