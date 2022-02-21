# 직사각형

'''
좌하, 우상 2개의 꼭짓점 좌표로 주어지는 2개의 직사각형

a: 겹치는 부분이 직사각형인 경우 (완전포함, 부분걸치기, 십자 걸치기)
b: 테두리만 line으로 접하기
c: 꼭짓점이 접하기
d: no 접점

'''

for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    sol = 'a'
    if p1 < x2 or y1 > q2 or x1 > p2 or q1 < y2:
        sol = 'd'
    elif p1 == x2 or x1 == p2:
        if q1 == y2 or y1 == q2:
            sol = 'c'
        else:
            sol = 'b'
    elif y1 == q2 or q1 == y2:
        sol = 'b'
    print(sol)
