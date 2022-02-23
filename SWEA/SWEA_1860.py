# 진기의 최고급 붕어빵

# 더 짧은 방법
for t in range(int(input())):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))
    # 리스트 정렬을 통해 가장 먼저 오는 손님이 언제인지 찾기
    # selection sort
    for i in range(N - 1):
        mini = i
        for j in range(i + 1, N):
            if lst[mini] > lst[j]:
                mini = j
        lst[i], lst[mini] = lst[mini], lst[i]

    sol = 'Possible'
    # second를 index로
    for i in range(N):
        # i + 1번째 손님이 온 순간 만들어 놓은 붕어빵
        cnt = (lst[i] // M) * K
        # i + 1번째 손님이 받을 수 있는 것보다 붕어빵 수가 적다면
        # i.e. 4초에 2개까지 만들 수 있는데 4초에 3번째 손님이라면
        if cnt < i + 1:
            sol = 'Impossible'
            break

    print(f'#{t + 1} {sol}')


# 내가 생각한 방법
for t in range(int(input())):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))
    # 리스트 정렬을 통해 가장 먼저 오는 손님이 언제인지 찾기
    # selection sort
    for i in range(N - 1):
        mini = i
        for j in range(i + 1, N):
            if lst[mini] > lst[j]:
                mini = j
        lst[i], lst[mini] = lst[mini], lst[i]

    sol = 'Possible'
    # second를 index로
    # 마지막 손님이 오는 순간까지의 붕어빵 개수 카운트할 리스트
    cnt = [0] * (lst[-1] + 1)
    i = M
    a = 1
    while i <= lst[-1]:
        cnt[i] = K * a
        i += 1
        if not i % M:
            a += 1
    for j in range(N):
        # 손님이 온 시간에 붕어빵이 0개면
        if cnt[lst[j]] <= 0:
            sol = 'Impossible'
            break
        for k in range(len(cnt) - lst[j]):
            cnt[lst[j] + k] -= 1

    print(f'#{t + 1} {sol}')