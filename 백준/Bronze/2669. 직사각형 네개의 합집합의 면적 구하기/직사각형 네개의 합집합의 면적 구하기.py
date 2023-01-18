board = [[0] * 101 for i in range(101)]
cnt = 0
for a in range(4):
    l,d,r,u = map(int,input().split())
    for i in range(l,r):
        for j in range(d,u):
            if board[i][j] == 0:
                cnt += 1
            board[i][j] = 1

print(cnt)