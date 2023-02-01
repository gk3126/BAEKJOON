n = int(input())
x = 0

for i in range(n):
    l = list(input().split())   # l을 리스트로 바꿔야 리버스가 사용이 가능함으로 l을 리스트로 변환.
    l.reverse()
    x += 1
    print('Case #%d: ' % (x), end='')   # 'Case #'으로 먼저 글을 받은 뒤. 문자 포매팅으로 숫자를 입력 받음.
    # print(*l)         # 앞에 *붙히면 값들이 원레대로 출력 됨. ([] 그리고 , 가 출력이 안된다.)
    for j in range(len(l)):     # 위에있는 것과 똑같음.
        print(l[j], end=" ")
    print()