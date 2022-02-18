# 요세푸스 문제

# 방법 1
# i = 0
N, K = map(int, input().split())
lst = list(range(1, N + 1))
sol = []
i = 0
while len(lst) > 0:
    i = (i + K) % len(lst) - 1
    if i < 0:
        i += len(lst)
    sol.append(lst.pop(i))
print(f'<{str(sol)[1:-1]}>')

# 방법 2
# i = -1
# 실행 시간이 더 짧다
N, K = map(int, input().split())
lst = list(range(1, N + 1))
sol = []
i = -1
while len(lst) > 0:
    i += K
    i %= len(lst)
    sol.append(lst.pop(i))
    i -= 1
print(f'<{str(sol)[1:-1]}>')