import sys
input = sys.stdin.readline

n = int(input())
per = []

for i in range(n):
    age,name = input().split()
    age = int(age)
    per.append([age,name])
    
per.sort(key= lambda x: x[0])

for i in range(n):
    print(per[i][0], per[i][1])