# 9단계 기본 수학2 택시 기하학
# 유클리드 기하학의 원과 택시 기하학에서의 원에 대한 문제

import math
import sys

r = int(sys.stdin.readline())
print(math.pi * r * r)
print(2 * r * r )

'''
택시 기하학에서의 원의 넓이는 밑변의 길이와 높이가 r인 삼각형 4개의 넓이의 합이다.

4 * (1/2 * w * h) = 2 * r * r

'''