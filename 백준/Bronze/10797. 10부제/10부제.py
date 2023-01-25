num = int(input())
a = 0
b,c,d,e,f = map(int,input().split())

s = [b,c,d,e,f]

for i in range(5):
    if s[i] == num:
        a += 1

print(a)