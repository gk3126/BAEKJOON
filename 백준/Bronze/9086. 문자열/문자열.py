n = int(input())

for i in range(n):
    t = list(input())
    a = t[0]
    t.reverse()
    print('%s%s' % (a,t[0]))