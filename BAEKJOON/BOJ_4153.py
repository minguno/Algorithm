# 9단계 기본 수학2 직각삼각형
# 피타고라스의 정리에 대해 배우는 문제

while 1:
    p = sorted(list(map(int, input().split())))
    if p[0]: break

    # 직각 삼각형의 조건
    if p[2] ** 2 == p[0] ** 2 + p[1] ** 2:
        print('right')
    else:
        print('wrong')