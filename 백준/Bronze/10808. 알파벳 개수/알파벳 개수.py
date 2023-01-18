from string import ascii_lowercase

alphabet_list = list(ascii_lowercase)

s = input()
count = dict()

for i in s:
    if i not in count:
        count[i] = 0
    count[i] += 1

for i in alphabet_list:
    if i not in count:
        print(0, end=" ")
    else:
        print(count[i], end=" ")