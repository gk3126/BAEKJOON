s = input()
for i in range(97,123):
    c = chr(i)
    if c in s:
        print(s.index(c), end= ' ')
    else:
        print(-1, end= ' ')
