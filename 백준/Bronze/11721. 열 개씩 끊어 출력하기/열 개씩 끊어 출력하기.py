a = input()
c = 0

for i in a:
    if c == 10:
        print()
        c = 0
    print(i,end="")
    c += 1