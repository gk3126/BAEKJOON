n = int(input())
fspace1 = n - 2
fspace2 = 1
print(' ' * (n - 1) + '*')

for i in range(n - 1):
    print(' ' * fspace1 + '*' + ' ' * fspace2 + '*')
    fspace1 -= 1
    fspace2 += 2