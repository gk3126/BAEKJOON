t = int(input())

for i in range(t):
    a,b = map(int,input().split(','))       # split으로 A,B로 구분을 지어서 할 수가 있음. 
                                            # 그냥 쓴다면 기본적으로 공백으로 구분이 됨.
    print(a + b)