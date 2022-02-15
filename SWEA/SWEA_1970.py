# 쉬운 거스름돈 

lst = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

T = int(input())
for t in range(T):
    N = int(input())
    c = [0] * 8
    for i in range(8):
        while N >= lst[i]:
            N -= lst[i]
            c[i] += 1
            if N == 0:
                break
    print(f'#{t + 1}')
    print(*c)