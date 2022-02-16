# 문자열의 거울상

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