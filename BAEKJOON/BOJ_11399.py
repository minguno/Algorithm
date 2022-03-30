# ATM

N = int(input())
lst = sorted(list(map(int, input().split())))
sol = 0
for i in range(N):
    sol += lst[i] * (N - i)
print(sol)