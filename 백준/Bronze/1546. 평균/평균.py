a = int(input())
b = list(map(int,input().split()))
m = max(b)
for i in range(a):
    b[i] = b[i]/m*100
c = sum(b)/a
print(c)