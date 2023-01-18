a = int(input())
for i in range(a):
    b,c = map(int,input().split())
    s = b + c
    print('Case #{0}: {1} + {2} = {3}'.format(i + 1, b, c, s))