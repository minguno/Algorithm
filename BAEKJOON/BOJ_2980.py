# 도로와 신호등
# 달팽이는 올라가고싶어가 생각남

N, L = map(int, input().split())
pos = 0
sol = 0
# 출발부터 마지막 신호까지 걸린 시간 계산
for _ in range(N):
    D, R, G = map(int, input().split())

    # 신호등까지 걸리 시간 (1m/sec)
    sol += D - pos
    # 현재 위치 갱신
    pos = D
    # 빨간불이 시작되고 지난 시간이 빨간불의 지속시간보다 짧다면
    # 차이만큼 대기해야함
    if sol % (R + G) < R:
        sol += R - (sol % (R + G))

# 마지막 신호부터 도착지점까지의 거리 계산
sol += L - pos

print(sol)