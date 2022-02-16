# Linked list 
# 숫자 추가

for t in range(int(input())):
    N, M, L = map(int, input().split())
    seq = list(map(int, input().split()))
    temp = []

    for _ in range(M):
        a, b = map(int, input().split())

        # a - 1 인덱스까지 원소들 pop
        for _ in range(N - a):
            temp.append(seq.pop())
        # append로 a 인덱스에 b 값 위치
        seq.append(b)

        # 다시 temp를 pop() 해서 뒷 원소들 순서대로 붙여주기
        for i in range(N - a):
            seq.append(temp.pop())

        # 리스트 길이 update
        N += 1

    print(f'#{t + 1} {seq[L]}')
    