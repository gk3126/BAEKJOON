n,k,m = map(int,input().split())
a = list(range(1,n + 1))
answer = []
i = 0

reverse_count = 0
reverse_order = False

for t in range(n):
    reverse_count += 1
    if not reverse_order:
        i += k - 1
    else:
        i -= k
    i %= len(a)
    answer.append(str(a[i]))
    del(a[i])
    if reverse_count == m:
        reverse_order = not reverse_order
        reverse_count = 0

print("\n".join(answer))