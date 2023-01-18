num = []
for i in range(5):
    num.append(int(input()))
for i in range(5):
    if num[i] < 40:
        num[i] = 40
print(sum(num) // 5)