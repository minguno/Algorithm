# 11단계 정렬


# 버블 정렬
lst = []
for _ in range(int(input())):
    lst.append(int(input()))

for i in range(len(lst) - 1):
    for j in range(i + 1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

for i in lst:
    print(i)

'''
시간 복잡도 문제 때문인지 틀렸다고 뜸

# 카운팅 정렬
N = int(input())
lst = [int(input()) for _ in range(N)]
temp = [0] * N
count = [0] * (max(lst) + 1)
for n in lst:
    count[n] += 1
for i in range(1, len(count)):
    count[i] += count[i - 1]
for i in range(N - 1, -1, -1):
    count[lst[i]] -= 1
    temp[count[lst[i]]] = lst[i]
for i in temp:
    print(i)

'''