num = [int(input()) for i in range(3)]
times = str(num[0] * num[1] * num[2])

for i in range(10):
    print(times.count(str(i)))
   