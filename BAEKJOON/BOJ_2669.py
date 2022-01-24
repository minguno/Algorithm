'''
백준에선 numpy 안됨

import numpy as np

grid = np.array([[0] * 100] * 100)

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            grid[i, j] = 1

count = 0
for i in grid:
    count += sum(i)

print(count)

'''

grid = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            grid[i][j] = 1

count = 0
for i in grid:
    count += sum(i)

print(count)


'''
Implications...

1. 2차원 배열 리스트를 만들 때 곱하기가 아닌 반복문으로 하기!
-> [[0] * 100] * 100 해버리면 안에 리스트 원소들이 복붙이 아닌 바로가기 생성 같은
원리로 만들어져 a[][] 인덱싱을 해도 모두 똑같이 적용됨

2. 여러개의 입력값에서 겹치는 부분을 제거해야하거나, 하나로 합쳐서 풀어야하는 문제들
e.g. 에라토스테네스의 체나 이것
은 T/F 로 구분해서 True만 출력하게 하거나 0, 1로 값을 줘서 1의 개수만 출력하거나
식으로 접근하기


'''