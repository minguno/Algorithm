# 색종이
# 정해진 범위에 같은 크기의 사각형이 겹쳐지게 올라올 때 총 면적 구하기
# 2669 문제와 풀이 방식이 유사

grid = [[False for _ in range(100)] for _ in range(100)]

for _ in range(int(input())):
    L = list(map(int, input().split()))
    for x in range(L[0], L[0] + 10):
        for y in range(L[1], L[1] + 10):
            if not grid[x][y]:
                grid[x][y] = True

area = 0
for i in grid:
    area += sum(i)

print(area)