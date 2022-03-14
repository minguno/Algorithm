# 숫자 카드2

# 방법 1 hash 연산
# list 연산은 시간복잡도가 너무 높아 시간초과
# 시간 848ms
N = input()
A1 = list(map(int, input().split()))
M = int(input())
B1 = list(map(int, input().split()))

hash = {}
for n in A1:
    if n in hash:
        hash[n] += 1
    else:
        hash[n] = 1
sol = [0] * M
for i in range(M):
    if B1[i] in hash:
        sol[i] = hash[B1[i]]
print(*sol)


# 방법 2 이분탐색
# 소요시간 3304ms
def bin(start, end, t):
    if start > end:
        return 0
    while start <= end:
        m = (start + end) // 2
        if t == A1[m]:
            return A1[start:end + 1].count(t)
        elif t < A1[m]:
            end = m - 1
        else:
            start = m + 1
    return 0


N = int(input())
A1 = sorted(list(map(int, input().split())))
A2 = set(A1)
M = int(input())
B1 = list(map(int, input().split()))

hash = {}
for i in range(N):
    s = 0
    e = N - 1
    if A1[i] not in hash:
        hash[A1[i]] = bin(s, e, A1[i])
sol = [0] * M
for i in range(M):
    if B1[i] in A2:
        sol[i] = hash[B1[i]]
print(*sol)