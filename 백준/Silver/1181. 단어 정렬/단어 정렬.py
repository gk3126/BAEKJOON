from re import X


n = int(input())
words = set()

for i in range(n):
    word = input()
    words.add(word)
    
words = sorted(words,key=lambda x: [len(x),x])

for i in range(len(words)):
    print(words[i])