num = int(input())

for i in range(1,num):
    a = i
    i = str(i)
    for c in i:
        a += int(c)
    if a == num:
        print(i)
        exit()

print(0)