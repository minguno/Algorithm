# 쇠막대기

lst = list(input())
cnt, sol = 0, 0

for i in range(len(lst)):
    if lst[i] == '(':
        cnt += 1
    else:
        if lst[i - 1] == '(':
            cnt -= 1
            sol += cnt
        else:
            cnt -= 1
            sol += 1

print(sol)