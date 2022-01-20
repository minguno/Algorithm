T = int(input())

for i in range(T):
    L = list(map(int, input().split()))
    A, B = L[0], L[1]
    print('Case #{}: {} + {} = {}'.format(i + 1, A, B, A + B))