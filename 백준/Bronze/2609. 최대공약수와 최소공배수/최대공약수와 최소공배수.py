from audioop import minmax


num1, num2 = map(int,input().split())

a = min(num1,num2)

for i in range(a,0,-1):
    if num1 % i == 0 and num2 % i == 0:
        print(i)
        print(num1 // i * num2 // i * i)
        break