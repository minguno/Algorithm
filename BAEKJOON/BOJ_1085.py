# 백준 9단계 기본 수학2 직사각형에서 탈출
# 직사각형과 점의 거리를 구하는 문제

x, y, w, h = map(int, input().split())

# 거리 1 = x, 거리 2 = y, 거리 3 = w - x, 거리 4 = h - y
distance = [x, y, w - x, h - y]

print(min(distance))