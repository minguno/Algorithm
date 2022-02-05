# 창고 다각형
# 인덱스 x값에 y값을 지정한 리스트의 sum() 구하기

# 좌표 받기
points = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    points.append((x, y))
points = sorted(points, key=lambda x: x[0])

# x 인덱스에 y 저장
# 인덱스 값이라 + 1 해줘서 갯수 맞추기
grid = [0] * (points[-1][0] + 1)
maxx, maxy = 0, 0
for idx, value in points:
    grid[idx] = value
    # 최대높이 기둥이 1개 이상일 수 있으니 이하로 처리
    if maxy <= value:
        maxy = value
        maxx = idx

# y최댓값 까지
total, value = 0, 0
for i in range(maxx + 1):
    if grid[i] > value:
        value = grid[i]
    total += value

# y최댓값 이후는 뒤집어서 똑같이
value = 0
for i in range(len(grid) - 1, maxx, -1):
    if grid[i] > value:
        value = grid[i]
    total += value

print(total)

'''
처음 접근했던 방법

사각형별로 w * h 해서 더하기
=> 최댓값이 하나 이상일 때 구현하기 꼬였음

'''