isPrime = [True] * 1001
isPrime[0] = False
isPrime[1] = False

for i in range(2, 1001):
    if isPrime[i]:
        for j in range(i * 2, 1001, i):
            isPrime[j] = False

n = int(input())
nums = list(map(int,input().split()))
answer = 0

for num in nums:
    if isPrime[num]:
        answer += 1
        
print(answer)