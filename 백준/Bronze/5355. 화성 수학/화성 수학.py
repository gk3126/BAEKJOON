fnum = int(input())
for i in range(fnum):
    a = input().split()
    num = float(a[0])
    for i in a[1:]:
        if i == '@':
            num *= 3
        elif i == '%':
            num += 5
        else:
            num -= 7
    print('{:.2f}'.format(num))