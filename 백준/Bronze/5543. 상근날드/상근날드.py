sb = int(input())
jb = int(input())
hb = int(input())
c = int(input())
s = int(input())

b = [sb,jb,hb]
d = [c,s]
b.sort()
d.sort()

print(b[0] + d[0] - 50)