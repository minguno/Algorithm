# 12단계 정렬

from collections import Counter
from sys import stdin
input= stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]

# mean
print(round(sum(lst) / N))

# median
lst.sort()
print(lst[N // 2])

# mode
c = Counter(lst).most_common()
# 원소가 1개거나 같은 수로만 이루어져 있을 때
    # 최고빈도수가 같을 때 두번째로 작은 값
if N == 1 or len(c) == 1:
    print(c[0][0])
else:
    if c[0][1] == c[1][1]:
        print(c[1][0])
    else:
        print(c[0][0])

# range
print(max(lst) - min(lst))