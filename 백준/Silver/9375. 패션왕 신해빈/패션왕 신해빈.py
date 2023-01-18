from collections import defaultdict

a = int(input())
for _ in range(a):
    n = int(input())
    type = defaultdict(int)
    answer = 1

    for i in range(n):
        c,t = input().split()
        type[t] += 1
        
    for i in type.values():
        answer *= i + 1
        
    print(answer - 1)