# 괄호
# 오른쪽 괄호와 왼쪽 괄호 수가 맞다면 cnt == 0, 오른쪽이 먼저 나오거나 더 많이 나오면
# cnt < 0, 왼쪽 괄호가 더 많아 짝이 맞지 않다면 cnt > 0

def is_vps(lit):
    cnt = 0
    for i in lit:    
        if i == "(":
            cnt += 1
        elif i == ")":
            cnt -= 1
        if cnt < 0:
            return 'NO'
    if cnt:
        return 'NO'
    return 'YES'

for _ in range(int(input())):
    print(is_vps(input()))