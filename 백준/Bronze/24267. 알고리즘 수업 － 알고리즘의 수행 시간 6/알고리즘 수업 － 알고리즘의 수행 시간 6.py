n = int(input())

n2 = n-2
sum = 0         # 함계 저장

for i in range(1, n-1):
    sum += n2 * i       # 1을 5번 곱하고 그 뒤로 차례대로 줄어들면서 밑에 있는 공식처럼 결과를 만들어 냄.
    n2 -= 1             # n을 줄이면서 곱하는 횟수를 줄어감.

print(sum)
print(3) 

# 35 =
# 5+4+3+2+1
#   4+3+2+1
#     3+2+1
#       2+1
#         1