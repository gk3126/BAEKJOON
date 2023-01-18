a = int(input())
for i in range(a):
    print(' ' * (a-i-1) + '*'* (1+i*2))
for i in range(1,a):
    print(' ' * i + '*' * (2*a-1-i*2))