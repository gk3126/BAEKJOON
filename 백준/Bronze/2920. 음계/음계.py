n = list(map(int,input().split()))
a = [1,2,3,4,5,6,7,8]
b = [8,7,6,5,4,3,2,1]

if n == a:
    print("ascending")
elif n == b:
    print("descending")
else:
    print("mixed")