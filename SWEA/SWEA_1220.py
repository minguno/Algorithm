# Magnetic

for t in range(10):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[j][i] == 1:
                k = j
                try:
                    while arr[k][i] != 2:
                        # 사이에 낀 1이 중복 카운트되면 안되니 값을 초기화
                        arr[k][i] = 0
                        k += 1
                    # 범위 안에서 2를 찾은거니 교착 상태 카운트
                    cnt += 1
                # 범위를 다 돌아도 2가 없다는 뜻이니 해당 column skip
                except IndexError:
                    break
    print(f'#{t + 1} {cnt}')
