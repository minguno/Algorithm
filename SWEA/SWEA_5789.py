# 현주의 상자 바꾸기

for t in range(int(input())):
    N, Q = map(int, input().split())
    # 1부터 N번의 상자 (범위 설정 편의를 위해 N+1개 생성)
    lst = [0 for _ in range(N + 1)]
    for i in range(1, Q + 1):
        l, r = map(int, input().split())
        for j in range(l, r + 1):
            lst[j] = i

    # 출력할 때 앞에 0자리 빼주기
    print(f'#{t + 1}', *lst[1:])