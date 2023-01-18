n = int(input())
fspace = n * 2 - 2
fstar = 1
for i in range(n):
    print('*' * fstar + ' ' * fspace + '*' * fstar)
    fstar += 1
    fspace -= 2
fstar -= 1
fspace += 2
for i in range(n - 1):
    fstar -= 1
    fspace += 2
    print('*' * fstar + ' ' * fspace + '*' * fstar)