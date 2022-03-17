# 랜선 자르기

def bin_search(t, lst):
    s = 1
    e = max(lst)
    while s <= e:
        m = (s + e) // 2
        temp = 0
        for i in range(len(lst)):
            temp += lst[i] // m
        # 개수가 크거나 같으면 자르는 길이를 늘려서 잘라봐도 된다
        if temp >= t:
            s = m + 1
        # 잘라서 나온 개수가 적으면 값을 낮춰서 잘라야 한다
        elif temp < t:
            e = m - 1
    return e


K, N = map(int, input().split())
lst = []
for _ in range(K):
    lst.append(int(input()))
print(bin_search(N, lst))