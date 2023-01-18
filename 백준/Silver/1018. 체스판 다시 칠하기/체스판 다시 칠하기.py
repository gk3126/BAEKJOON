n,m = map(int,input().split())
b = [
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB'
    ]
w = [
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW'
    ]
ch = []

for i in range(n):
    a = input()
    ch.append(a)
    
minanswer = 9999999
    
for i in range(n - 8 + 1):
    for j in range(m - 8 + 1):
        banswer = 0
        wanswer = 0

        for o in range(8):
            for p in range(8):
                if ch[o + i][p + j] != b[o][p]:
                    banswer += 1

        for o in range(8):
            for p in range(8):
                if ch[o + i][p + j] != w[o][p]:
                    wanswer += 1
            
        answer = min(wanswer,banswer)
        minanswer = min(answer,minanswer)

print(minanswer)