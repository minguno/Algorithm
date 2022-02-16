# GNS

# 방법 1
# 카운팅 정렬과 딕셔너리를 병합한 문자열 오름차순 정렬

dct = {
    'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR':3,
    'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7,
    'EGT': 8, 'NIN': 9
}

for _ in range(int(input())):
    t, N = input().split()
    src = list(input().split())
    temp = [0] * int(N)
    c = [0] * 10
    for i in range(int(N)):
        c[dct[src[i]]] += 1

    for i in range(1, 10):
        c[i] += c[i - 1]

    for i in range(int(N)):
        c[dct[src[i]]] -= 1
        temp[c[dct[src[i]]]] = src[i]

    print(t)
    print(*temp)


# 방법 2
# sorted() 와 딕셔너리 써서 value 값에 대해 오름차순 정렬

dct = {
    'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR':3,
    'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7,
    'EGT': 8, 'NIN': 9
}

for _ in range(int(input())):
    t, N = input().split()
    src = list(input().split())
    sol = list(sorted(src, key=lambda x: dct[x]))
    print(t)
    print(*sol)