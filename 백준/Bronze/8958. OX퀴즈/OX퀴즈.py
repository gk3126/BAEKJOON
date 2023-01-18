a = int(input())
for i in range(a):
    b = input()
    point = 0
    streak = 0
    for j in range(len(b)):
        if b[j] == 'O':
            streak += 1
            point += streak
        elif b[j] == 'X':
            streak = 0
    print(point)    