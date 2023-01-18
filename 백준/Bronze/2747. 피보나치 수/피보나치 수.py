n = int(input())
num = [-1] * (n + 1)
num[0] = 0
num[1] = 1

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    if num[n] != -1:
        return num[n]
    num[n] = fibo(n - 2) + fibo(n - 1)
    return num[n]
print(fibo(n))