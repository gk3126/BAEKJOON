n,m = map(int,input().split())
a = list(map(int,input().split()))
c = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            point = a[i] + a[k] + a[j]
            if point > c and point <= m:
                c = point
                
print(c)