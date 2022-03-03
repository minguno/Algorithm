# 진법 변환 2
# 계속 나누면서 나머지를 리스트에 추가하는데
# 추가된 나머지는 원래는 뒤에서부터 집어넣는 것이므로 나중에 결과를 뒤집는다

# 방법 1
num_dict = {k - ord('A') + 10: chr(k) for k in range(ord('A'), ord('Z') + 1)}
N, K = map(int, input().split())
sol = []
md = 0

while N > 0:
    md = N % K

    if md >= 10:
        sol.append(num_dict[md])
    else:
        sol.append(md)
    N //= K

print(*sol[::-1], sep='')

# 방법 2
def ja(n):
    if 0 <= int(n) <= 9:
        return str(n)
    else:
        return chr(n + 55)


N, B = map(int, input().split())
total = ''
while N > 0:
    total += ja(N % B)
    N //= B
print(total[::-1])