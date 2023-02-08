n = int(input())
c = n

for i in range(n):
    a = input()
    for index in range(len(a) - 1):             # 단어의 처음부터 비교, -1을 한 이유는 현재 위치와 다음 위치를 비교할 예정
        if(a[index] != a[index + 1]):           # 현재위치의 알파벳과 다음 위치의 알파벳이 다를 경우, 그룹단어인 경우
            if a[index + 1] in a[:index]:       # 다음 위치의 알파벳이 현재위치 이전에 알파벳에 있을 경우, 즉 그룹단어가 아님
                c -= 1
                break                           # 브레이크의 이유는 중간에서 그룹단어가 아닌걸 확인을 했는데, 더 이상 확인할 필요가 없어서. 여기서 브레이크를 안하면 위에 c -= 1이 삐져나감
print(c)