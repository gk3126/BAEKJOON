def next_alpha(c):
    c = chr(ord(c) + 1)
    if c == "{":
        c = "a"
    elif c == "[":
        c = "A"
    return c

def next(s):
    a = ""
    for c in s:
        a += next_alpha(c)
    return a

c = input()

for i in range(23):
    c = next(c)

print(c)