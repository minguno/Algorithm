N = list(map(int, input().split()))

L = []
a = list(map(int, input().split()))
for i in a:
    if i < N[1]:
        L.append(i)
print(*L)