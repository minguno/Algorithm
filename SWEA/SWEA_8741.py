# 두문자어

for t in range(int(input())):
    s = input().split()
    sol = ''
    for i in s:
        sol += i[0].upper()
    print(f'#{t + 1} {sol}')