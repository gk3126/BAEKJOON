import sys
input = sys.stdin.readline

n,m,b = map(int,input().split())
a = []
maxh = 0
minh = 0
answert = 999999999999
answerh = 999999999999
ablock = b

for i in range(n):
    l = list(map(int,input().split()))
    maxh = max(maxh,max(l))
    minh = min(minh,min(l))
    ablock += sum(l)
    a.append(l)

makemax = ablock // (n * m)

for h in range(minh,min(makemax,maxh) + 1):
    t = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] < h:
                t += h - a[i][j]
            else:
                t += (a[i][j] - h) * 2
    if t <= answert:
        answert = t
        answerh = h

print(answert, answerh)