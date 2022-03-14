# 수 찾기

_ = input()
A = set(list(map(int, input().split())))
M = int(input())
lst = list(map(int, input().split()))

for i in range(M):
    print(1 if lst[i] in A else 0)