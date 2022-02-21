# 두 개의 숫자열

for t in range(int(input())):
    N, M = map(int, input().split())
    arrN = list(map(int, input().split()))
    arrM = list(map(int, input().split()))
    sol = 0
    if N > M:
        N, M = M, N
        arrN, arrM = arrM, arrN
    for i in range(M - N + 1):
        cnt = 0
        for j in range(N):
            cnt += arrN[j] * arrM[i + j]
        if sol < cnt:
            sol = cnt

    print(f'#{t + 1} {sol}')
