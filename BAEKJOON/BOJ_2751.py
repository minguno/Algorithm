# 11단계 정렬
# 시간 복잡도가 O(nlogn)인 정렬 알고리즘으로 풀 수 있다 e.g. 병합, 힙 등

from sys import stdin
input = stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]
lst.sort()
for i in lst:
    print(i)