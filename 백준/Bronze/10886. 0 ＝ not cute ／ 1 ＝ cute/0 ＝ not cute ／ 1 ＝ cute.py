a = int(input())
Jcute = 0
Jncute = 0
for i in range(a):
    b = int(input())
    if b == 1:
        Jcute += 1
    elif b == 0:
        Jncute += 1
if Jcute > Jncute:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')