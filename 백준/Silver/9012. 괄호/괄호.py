num = int(input())
for i in range(num):
    a = input()
    s = []
    p = "YES"
    for c in a:
        if c == "(":
            s.append("(")
        else:
            if s:
                s.pop()
            else:
                p = "NO"
    if not s and p == "YES":
        print("YES")
    else:
        print("NO")