# 회의실 배정
# 정렬을 하는 방식이 관건
# 둘 다 4초

# 방법 1
N = int(input())
lst = sorted(list(list(map(int, input().split())) for _ in range(N)), key=lambda x: (x[1], x[0]))
sol = temp = 0
for s, e in lst:
    if s >= temp:
        temp = e
        sol += 1
print(sol)

# 방법 2
N = int(input())
lst = [tuple(map(int, input().split())) for _ in range(N)]
lst.sort(key=lambda x: x[0])
lst.sort(key=lambda x: x[1])
sol = temp = 0
for s, e in lst:
    if s >= temp:
        sol += 1
        temp = e
print(sol)