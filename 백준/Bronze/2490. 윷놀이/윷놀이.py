for i in range(3):
    a,b,c,d = map(int,input().split())          # 하나가 아닌 여러개를 3번 받는다.

    s = [a,b,c,d]       # 어펜드가 아닌 간단한 방법으로 리스트에 넣는 방법.

    o = 0

    for i in range(4):
        if s[i] == 1:
            o += 1

    if o == 3:
        print('A')
    elif o == 2:
        print('B')
    elif o == 1:
        print('C')
    elif o == 0:
        print('D')
    elif o == 4:
        print('E')