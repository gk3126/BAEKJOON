n = int(input())
pw = []
ph = []
answer = []

for i in range(n):
    x,y = map(int,input().split())
    pw.append(x)
    ph.append(y)
    
for i in range(n):
    cnt = 0
    for j in range(n):
        if i == j:
            continue
        if pw[j] > pw[i] and ph[j] > ph[i]:
            cnt += 1
    answer.append(cnt + 1)
    
print(*answer)