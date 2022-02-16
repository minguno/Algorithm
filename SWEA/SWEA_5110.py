# Linked list
# 수열 합치기

# 제공된tc에 한해선 아래 방법이 수행 시간이 더 짧았음
for t in range(int(input())):
    N, M = map(int, input().split())
    # 시작 수열
    seq = list(map(int, input().split()))
    temp = []
    sol = []
    n = N
    for _ in range(M - 1):
        new = list(map(int, input().split()))
        flag = True
        for i in range(N):
            if seq[i] > new[0]:
                flag = False
                seq[i: i] = new
                break
        if flag:
            seq.extend(new)
        N += n

    for _ in range(10):
        sol.append(seq.pop())

    print(f'#{t + 1}', *sol)

'''
3중 for문 때문에 시간초과 난 줄 알고 밖으로 빼 줌.
-> 그래도 똑같

for t in range(int(input())):
    N, M = map(int, input().split())
    # 시작 수열
    seq = list(map(int, input().split()))
    temp = []
    sol = []
    n = N
    for _ in range(M - 1):
        new = list(map(int, input().split()))
        flag = True
        for i in range(N):
            if seq[i] > new[0]:
                flag = False
                idx = i
                break
        if flag:
            seq.extend(new)
        else:
            for _ in range(N - idx):
                temp.append(seq.pop())
            seq.extend(new)
            for _ in range(N - idx):
                seq.append(temp.pop())

        # seq 길이 update
        N += n

    for _ in range(10):
        sol.append(seq.pop())

    print(f'#{t + 1}', *sol)
'''
'''
처음 구현한 방식
-> 시간 초과 (2초)

for t in range(int(input())):
    N, M = map(int, input().split())
    # 시작 수열
    seq = list(map(int, input().split()))
    
    temp = []
    sol = []

    # 수열 추가 작업
   for _ in range(M - 1):
        new = list(map(int, input().split()))
        flag = True
        # 사이에 삽입
        for i in range(N):
            if seq[i] > new[0]:
                flag = False
                for _ in range(N - i):
                    temp.append(seq.pop())
                seq.extend(new)
                for _ in range(N - i):
                    seq.append(temp.pop())
                break
        # 중간 삽입 안이루어졌을 시 맨 뒤에 붙이기
        if flag:
            seq.extend(new)
        # seq 길이 update
        N += M

    for _ in range(10):
        sol.append(seq.pop())
    print(f'#{t + 1}', *sol)
'''