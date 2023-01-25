x = int(input())
y = int(input())

if x <= -1 and y <= -1:
    print('3')
    
if x >= 1 and y >= 1:
    print('1')
    
if x <= -1 and y >= 1:
    print('2')
    
if x >= 1 and y <= -1:
    print('4')