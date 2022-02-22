# 농작물 수확하기
# 가운데 row부터 시작하기

for t in range(int(input())):
    N = int(input())
    arr = [input() for _ in range(N)]
    sol = 0
    i, k = N // 2, 0
    while k <= N // 2:
        for j in range(0 + k, N - k):
            if not k:
                sol += int(arr[i][j])
            else:
                sol += int(arr[i + k][j])
                sol += int(arr[i - k][j])
        k += 1
    print(f'#{t + 1} {sol}')