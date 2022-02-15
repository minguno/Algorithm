# 파리 퇴치

for t in range(int(input())):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    sol = 0
    # 유효 범위 정하는 것 주의
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            ssum = 0
            # 좌측 상단 모서리 좌표를 기준으로 M영역
            for k in range(M):
                for l in range(M):
                    ssum += grid[i + k][j + l]

            if sol < ssum:
                sol = ssum
    print(f'#{t + 1} {sol}')