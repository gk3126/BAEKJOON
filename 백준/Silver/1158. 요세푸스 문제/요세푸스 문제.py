n,k = map(int,input().split())
a = list(range(1,n + 1))
answer = []
i = 0

for _ in range(n):
    i += k - 1
    i %= len(a)
    answer.append(str(a[i]))
    del(a[i])

print("<" + ", ".join(answer) + ">")