# 경비원
# 상점의 사방 중 위치와 동근이의 4방 위치에 따른 조건식 걸기
'''
1, 2 -> 북, 남. 왼쪽 기준
3, 4 -> 왼, 오. 위쪽 기준

'''

w, h = map(int, input().split())
n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
x = list(map(int, input().split()))

sol = 0
for i in range(n):
    # 상점이 북쪽일 때
    if lst[i][0] == 1:
        if x[0] == 1:
            sol += abs(lst[i][1] - x[1])
        elif x[0] == 2:
            sol += min(x[1] + h + lst[i][1], w - x[1] + h + w - lst[i][1])
        elif x[0] == 3:
            sol += x[1] + lst[i][1]
        else:
            sol += x[1] + w - lst[i][1]
    # 상점이 남쪽일 때
    elif lst[i][0] == 2:
        if x[0] == 1:
            sol += min(x[1] + h + lst[i][1], w - x[1] + h + w - lst[i][1])
        elif x[0] == 2:
            sol += abs(lst[i][1] - x[1])
        elif x[0] == 3:
            sol += h - x[1] + lst[i][1]
        else:
            sol += h - x[1] + w - lst[i][1]
    # 상점이 서쪽일 때
    elif lst[i][0] == 3:
        if x[0] == 1:
            sol += x[1] + lst[i][1]
        elif x[0] == 2:
            sol += x[1] + h - lst[i][1]
        elif x[0] == 3:
            sol += abs(lst[i][1] - x[1])
        else:
            sol += min(x[i] + w + lst[i][1], h - x[1] + w + h - lst[i][1])
    # 상점이 동쪽일 때
    else:
        if x[0] == 1:
            sol += w - x[1] + lst[i][1]
        elif x[0] == 2:
            sol += w - x[1] + h - lst[i][1]
        elif x[0] == 3:
            sol += min(x[i] + w + lst[i][1], h - x[i] + w + h - lst[i][1])
        else:
            sol += abs(lst[i][1] - x[1])

print(sol)
