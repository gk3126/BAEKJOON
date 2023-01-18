w = input().upper()
a = dict()
for i in w:
    if i not in a:
        a[i] = 0
    a[i] += 1
m = ''
f = 0
for i in a:
    if a[i] > f:
        f = a[i]
        m = i
    elif a[i] == f:
        m = '?'
print(m)