a,b = map(int,input().split())
if b >= 45:
    b -= 45
else:
    a -= 1
    b += 15
if a == -1:
    a += 24
print(a,b)