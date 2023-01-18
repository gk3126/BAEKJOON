import sys
input = sys.stdin.readline

n = int(input())
nums = []

for i in range(n):
    x,y = map(int,input().split())
    nums.append([x,y])
    
nums.sort(key= lambda x: [x[1],x[0]])

for i in range(n):
    print(nums[i][0], nums[i][1])