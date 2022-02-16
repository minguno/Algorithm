# Ladder 2
# 도착점은 다 똑같이 1이고 최단 거리로 도착하는 사다리 좌표를 구하라
# 복수개면 좌표값이 가장 큰 걸 출력하라

for _ in range(10):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    sol, Idx = int(1e8), 0
    # 출발지점
    for x in range(100):
        if arr[0][x]:
            i, j = 0, x
            cnt = 0
            while i < 99:
                # 오른쪽 이동
                if j < 99 and arr[i][j + 1]:
                    # 0 만나면 이동 stop
                    while j < 99 and arr[i][j + 1] != 0:
                        j += 1
                        cnt += 1
                # 왼쪽 이동
                elif j > 0 and arr[i][j - 1]:
                    dir = 2
                    # 0 만나면 이동 stop
                    while j > 0 and arr[i][j - 1] != 0:
                        j -= 1
                        cnt += 1
                # 좌우 이동 외엔 항상 하향 이동
                i += 1
                cnt += 1
            if sol >= cnt:
                sol = cnt
                Idx = x

    print(f'#{t} {Idx}')