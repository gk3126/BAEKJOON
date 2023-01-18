from re import A
import sys
sys.setrecursionlimit(100000)

a = int(input())
for i in range(a):
    
    n = int(input())

    num = [-1] * (n + 2)
    num[0] = 1
    num[1] = 0

    def fibo2(n):
        if n == 0:
            return 1
        elif n == 1:
            return 0
        if num[n] != -1:
            return num[n]
        num[n] = fibo2(n - 2) + fibo2(n - 1)
        return num[n]
    print(fibo2(n))

    num1 = [-1] * (n + 2)
    num1[0] = 0
    num1[1] = 1

    def fibo(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        if num1[n] != -1:
            return num1[n]
        num1[n] = fibo(n - 2) + fibo(n - 1)
        return num1[n]
    print(fibo(n))

