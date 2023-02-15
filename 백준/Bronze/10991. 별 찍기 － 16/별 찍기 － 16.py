n = int(input())

for i in range(1, n + 1, 1):
    
    for j in range(1, n+1-i, 1):
        print(' ', end="")
        
    for j in range(0, i, 1):
        print('* ', end="")
        
    print()

# 또 다른 방법
# for i in range(1, n + 1):
#   print(' ' * (n - i) + '* ' * (i - 1) + '*')