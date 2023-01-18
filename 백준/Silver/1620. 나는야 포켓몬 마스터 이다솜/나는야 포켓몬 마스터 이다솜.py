import sys
input = sys.stdin.readline

n,m = map(int,input().split())
pokemon = []
pokemond = dict()

for i in range(n):
    a = input().rstrip()
    pokemon.append(a)
    pokemond[a] = i + 1
    
for i in range(m):
    q = input().rstrip()
    if q.isalpha():
        print(pokemond[q])
    else:
        q = int(q)
        print(pokemon[q - 1])