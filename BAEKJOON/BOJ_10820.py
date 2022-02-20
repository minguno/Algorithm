# 문자열 분석

from sys import stdin
rd = stdin.readline

N = 1
while N:
    # 오른쪽에 공백 문자가 들어올 수 있으니 줄바꿈으로 특정해주기
    s = rd().rstrip('\n')
    # input이 비었거나 100줄까지 밭았으면
    if not s or (N > 100):
        break
    # lower, upper, digit, space
    sol = [0 for _ in range(4)]
    for c in s:
        if c.islower():
            sol[0] += 1
        elif c.isupper():
            sol[1] += 1
        elif c.isdigit():
            sol[2] += 1
        else:
            sol[3] += 1
    print(*sol)
    N += 1