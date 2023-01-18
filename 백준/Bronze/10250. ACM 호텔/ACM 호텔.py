num = int(input())
for i in range(num):
    h, w, n = map(int,input().split())
    nh = (n - 1) % h + 1
    nw = (n - 1) // h + 1
    if nw < 10:
        answer = str(nh) + "0" + str(nw)
    else:
        answer = str(nh) + str(nw)
    print(answer)