a = int(input())
for o in range(a):
    Ycount = 0
    Kcount = 0
    for i in range(9):
        b,c = map(int,input().split())
        Ycount += b
        Kcount += c
    if Ycount > Kcount:
        print('Yonsei')
    elif Kcount > Ycount:
        print('Korea')
    else:
        print('Draw')