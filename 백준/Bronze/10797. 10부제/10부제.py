num = int(input())
a = 0
b,c,d,e,f = map(int,input().split())

s = [b,c,d,e,f]

for i in range(5):
    if s[i] == num:
        a += 1

print(a)

# 이런 식으로도 풀기 가능.
# n = int(input())
# car = list(map(int,input().split())) (입력한 정수를 띄어쓰기로 구분하여 리스트에 저장.)
# print(car.count(n))