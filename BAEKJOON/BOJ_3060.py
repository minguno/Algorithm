# 욕심쟁이 돼지

dct = {}
for i in range(6):
    dct[i] = [i, (i + 1) % 6, (i + 3) % 6, (i + 5) % 6]

for t in range(int(input())):
    N = int(input())
    lst = list(map(int, input().split()))
    sol = 1
    while sum(lst) <= N:
        temp = []
        for i in range(6):
            n = 0
            for x in dct[i]:
                n += lst[x]
            temp.append(n)
        lst = temp
        sol += 1
    print(sol)