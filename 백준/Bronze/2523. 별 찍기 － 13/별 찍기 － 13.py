# 한번에 출력하는 것이 아닌 상단 하단으로 나눈 후 각각 출력
n = int(input())

# 상단
for i in range(1, n + 1, 1):
    print('*' * i)

# 하단
for i in range(1, n, 1):
    print('*' * (n - i))