from re import S


n = int(input())
if n == 1:
    print(1)
    exit()
f = 2
s = 2

while True:
    if s <= n < s + (f - 1) * 6:
        break
    s += (f - 1) * 6
    f += 1
    
print(f)