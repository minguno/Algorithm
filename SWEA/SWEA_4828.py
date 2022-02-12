# min max

T = int(input())
for t in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    minn = int(1e8)
    maxx = -int(1e8)
    for num in lst:
        if minn > num:
            minn = num
        if maxx < num:
            maxx = num

    print(f'#{t + 1} {maxx - minn}')