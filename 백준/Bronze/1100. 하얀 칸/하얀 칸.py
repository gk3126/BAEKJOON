a = []
count = 0

for i in range(8):
    c = input()
    a.append(c)

for i in range(8):
    for j in range(8):
        if a[i][j] == "F" and (i + j) % 2 == 0:
            count += 1

print(count)