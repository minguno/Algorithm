# 전기 버스
# 총 정류장 수 N, 충전소 수 K, K보유 정류장 수 M

T = int(input())
for t in range(T):
    K, N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    i, j = 0, 0
    cnt = 0

    while i + K < N:
        # 정류장 간격이 최대 이동거리 K보다 크다면 0 출력하는 예외처리
        if i + K < lst[j]:
            cnt = 0
            break
        # 최대 이동거리와 가장 가까운 충전소가 나올 때 까지 반복
        while i + K >= lst[j]:
            j += 1
            # 충전소 리스트 인덱스 범위를 벗어나면 반복문 종료
            if j > (M - 1):
                break
        # 최대 이동거리에서 가장 가까운 전 정류장으로 현재 위치 지정
        i = lst[j - 1]
        # 충전 횟수
        cnt += 1

    print(f'#{t + 1} {cnt}')

'''
아래는 참고할 만한 다른 풀이 방식이다. 메모리 사용량과 실행 시간이 좀 더 짧다.
-> if~ else문을 잘 이용하는 것이 시간 복잡도를 줄이는 key이다

# 김연준 풀이

T = int(input())
for t in range(T):
    K, N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    i = 0
    cnt = 0
    while i < N:
        search = 0
        # 최대 거리부터 하나씩 감소해서 가장 가까운 정류장에서 멈추기
        for k in range(K, 0, -1):
            # 충전할 필요가 없을 때
            if (i + k) >= N:
                i = N
                break
            # 최대 이동 거리에 충전소가 있을 때
            elif (i + k) in lst:
                cnt += 1
                i = i+k
                break
            else:
                search += 1
        # 최대 이동거리 안에 충전소가 없을 때 cnt 초기화시키고 while문 종료
        if search == K:
            cnt = 0
            break

print(f'#{t+1} {cnt}')
'''