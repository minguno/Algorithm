# 암호문 1

for t in range(10):
    N = input()
    lst = input().split()
    _ = input()
    cmd = input().split()
    i = 0
    while i < len(cmd):
        pos = int(cmd[i + 1])
        cnt = int(cmd[i + 2])
        if pos < 10:
            for j in range(cnt):
                lst.insert(pos + j, cmd[i + 3 + j])
        i += 3 + cnt

    print(f'#{t + 1}', *lst[:10])