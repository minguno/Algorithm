# 행운의 바퀴

N, K = map(int, input().split())
lst = ['?'] * N
p = 0
sol = 0
for _ in range(K):
    S, l = input().split()
    if p - int(S) < 0:
        p = (p - int(S) + N) % N
    else:
       p = (p - int(S)) % N
    if (lst[p] == '?' and l not in lst) or lst[p] == l:
        lst[p] = l
    else:
        sol = 1
        break
if sol:
    print('!')
else:
    print(''.join(lst[p:]+lst[:p]))