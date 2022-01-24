# 8단계 기본 수학1 부녀회장이 될테야
# 층과 거주자 수의 규칙을 찾는 문제
'''
k range(k + 1)
n range(1, n + 1)
0층에는 호 = 명수

k = 0, n = 1, p = 1
k = 0, n = 2, p = 2
k = 0, n = 3, p = 3
.
.
.
k = 0, n = n, p = n

k = 1, n = 1, p = 1
k = 1, n = 2, p = 1 + 2 = 3
k = 1, n = 3, p = 1 + 2 + 3 = sum(range(1, 4)) = 6
.
.
.
k = 1, n = n, p = sum(range(1, n + 1))

k = 2, n = 1, p = 1
k = 2, n = 2, p = 1 + (1 + 2)
k = 2, n = 3, p = 1 + (1 + 2) + (1 + 2 + 3) = 1 + 3 + 6 = 10
.
.
.
k = 2, n = n, p = for i in range(1, n + 1): peeps += sum(range(1, i + 1))

'''
T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    # 시작인 0 층에 대한 리스트
    k0 = [x for x in range(1, n + 1)]
    # k - 1층까지의 사람들의 합이니 인덱스에 그냥 k를 넣어준다
    # k - 1층까지 도달할 때까지 0층부터 사람수를 누적합할 거다
    for _ in range(k):
        # 각 호실의 인덱스로 사용할 i인데 마지막 값이 i - 1이니 최대 범위가
        # n + 1이 아니라 n으로 설정
        for i in range(1, n):

            k0[i] += k0[i - 1]

    print(k0[-1])

'''
Implications...

1. 1씩 증가하는 수열이 주어졌다면 무조건 인덱스로 활용할 생각하기!

2. x, y 혹은 가로, 세로 혹은 width, height 와 같이 옆, 위로 뻗어나가는 문제에선
for 문을 2번 연속으로 써서 교차하게 해준다.

'''