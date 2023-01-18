def next(n):
    a = n % 10
    b = n // 10
    return a * 10 + ((a + b) % 10)

a = int(input())
num = next(a)
c = 1

while num != a:
    num = next(num)
    c += 1
    
print(c)