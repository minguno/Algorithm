T = int(input())

for i in range(T):
    L = list(map(int, input().split()))
    print('Case #{}: {}'.format(i + 1, L[0] + L[1]))