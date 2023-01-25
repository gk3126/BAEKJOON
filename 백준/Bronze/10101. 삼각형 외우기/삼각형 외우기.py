a = int(input())
b = int(input())
c = int(input())
t = a + b + c
    
if t == 180:
    if a == 60 and b == 60 and c == 60:
        print('Equilateral')
    elif a == b or a == c or c == b:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print("Error")