# 나무 자르기

def BinSearch(t, arr):
    s = 1
    e = max(arr)
    while s <= e:
        m = (s + e) // 2
        temp = 0
        for i in arr:
            if i >= m:
                temp += i - m
        if temp >= t:
            s = m + 1
        else:
            e = m - 1
    return e


N, M = map(int, input().split())
lst = list(map(int, input().split()))
print(BinSearch(M, lst))
