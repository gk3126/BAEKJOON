import itertools 

answer = [list(range(1,15))]
for i in  range(14):
    answer.append(list(itertools.accumulate(answer[-1])))

t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())
    print(answer[k][n - 1])