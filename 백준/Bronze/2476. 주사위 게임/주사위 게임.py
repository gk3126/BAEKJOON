def get_reward(a,b,c):
    if a == b == c:
        return 10000 + b * 1000
    elif  a == b:
        return 1000 + b * 100
    elif  a == c:
        return 1000 + a * 100
    elif  b == c:
        return 1000 + b * 100
    else:
        return max(a,b,c) * 100
    
N = int(input())
answer = 0
for i in range(N):
    a,b,c = map(int,input().split())
    answer = max(answer,get_reward(a,b,c))
    
print(answer)