import math

T = int(input())

N = list(map(int, input().split()))

M = max(N)
print((sum(N) / M * 100) / T)
