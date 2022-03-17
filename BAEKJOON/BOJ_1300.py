# K번째 수

def b_search(start, end):
    ans = 0

    while start <= end:
        mid = (start + end) // 2
        sm = 0
        for i in range(1, N + 1):
            sm += min(mid // i, N)

        if sm >= k:
            ans = mid
            end = mid - 1

        elif sm < k:
            start = mid + 1

    return ans


N = int(input())

k = int(input())
s = 1
e = N * N
print(b_search(s, e))