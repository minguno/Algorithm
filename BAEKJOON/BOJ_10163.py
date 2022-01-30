# 순서대로 겹쳐진 색종이의 최종 보여지는 면적 각각 구하기
# 색종이를 1, 2, 3 ... 이렇게 번호를 매겨 그 값으로 해당 인덱스 값을 지정해줬다
# 그 후 count() 메서드로 각 색종이의 최종 면적을 출력

import sys

grid = [[0 for _ in range(1001)] for _ in range(1001)]


N = int(sys.stdin.readline())

areas = []

for n in range(1, N + 1):
    a, b, w, h = map(int, sys.stdin.readline().split())

    for i in range(1000 - b, 1000 - b - h, -1):
        for j in range(a, a + w):
            grid[i][j] = n

for n in range(1, N + 1):
    total = 0
    for i in grid:
        total += i.count(n)
    print(total)