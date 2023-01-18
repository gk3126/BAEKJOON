t = int(input())
for i in range(t):
    n,w = input().split()
    n = int(n)
    w2 = ''
    for j in w:
        w2 += n * j
    print(w2)