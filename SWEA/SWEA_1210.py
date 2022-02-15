# Ladder 1

for _ in range(10):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    
    # 목표지점 찾기
    for x in range(100):
        if arr[99][x] == 2:
            j = x
    
    i = 99
    
    while i > 0:
        # 오른쪽 이동
        if j < 99 and arr[i][j + 1]:
            # 0 만나면 이동 stop
            while j < 99 and arr[i][j + 1] != 0:
                j += 1
        
        # 왼쪽 이동
        elif j > 0 and arr[i][j - 1]:
            dir = 2
            # 0 만나면 이동 stop
            while j > 0 and arr[i][j - 1] != 0:
                j -= 1
        
        # 좌우 이동 외엔 항상 상향 이동
        i -= 1

    print(f'#{t} {j}')