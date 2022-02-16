# 문자열의 거울상

# 방법 1
for t in range(int(input())):
    p = input()
    q = p[::-1]
    sol = ''
    for i in range(len(p)):
        if q[i] == 'b':
            sol += 'd'
        elif q[i] == 'd':
            sol += 'b'
        elif q[i] == 'p':
            sol += 'q'
        else:
            sol += 'p'
    print(f'#{t+1} {sol}')

# 방법 2
dct = {'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'}

for t in range(int(input())):
    word = input()
    sol = ''
    for i in range(len(word) - 1, -1, -1):
        sol += dct[word[i]]
    print(f'#{t + 1} {sol}')