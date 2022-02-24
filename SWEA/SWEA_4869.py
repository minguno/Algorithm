# 종이붙이기

for t in range(int(input())):
    N = int(input())
    N //= 10
    lst = [0] * (N + 1)
    lst[1], lst[2] = 1, 3
    for i in range(3, N + 1):
        lst[i] = lst[i - 1] + lst[i - 2] * 2

    # lst의 마지막 원소 출력
    print(f'#{t + 1} {lst[N]}')