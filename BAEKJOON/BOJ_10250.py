# 8단계 기본 수학1 ACM 호텔
# 호첼 방 번호의 규칙을 찾아 출력하는 문제

# test case number
T = int(input())

for _ in range(T):
    # H를 몇번 반복해야 하는지
    cycle = 1
    H, W, N = map(int, input().split())
    while N > H  * cycle:
        cycle += 1

    # 호수를 나타내는 값
    X = cycle
    # 층수를 나타내는 값
    Y = N - H * (cycle - 1)
    
    print(f'{Y}{X:02d}')
