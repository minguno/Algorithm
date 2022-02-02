# 9단계 기본 수학2 터렛
# 두 원의 교점의 개수를 구하는 문제

import math

for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    # 두 원의 거리 구하기
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    # 두 원이 완전히 겹칠 때
    if distance == 0 and r1 == r2:
        print(-1)
    
    # 외접, 내접일 때
    elif r1 + r2 == distance or abs(r1 - r2) == distance:
        print(1)
    
    # 두 개의 교차점이 있을 때
    elif abs(r1 - r2) < distance < (r1 + r2):
        print(2)
    
    # 한 원이 다른 원의 내부에 있거나 그 밖에 교점이 없을 때
    else:
        print(0)
