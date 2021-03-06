# 개미

from sys import stdin
input = stdin.readline

'''
t가 최대 2억이기 때문에 일일히 방향 전환을 delta로 계산하면 무조건
런타임 에러다.

개미는 기본적으로 1 시간(t)당 양 옆과 위 아래로 1칸씩 움직인다(+던 -이던).
p+t를 w로 나눠주면 0~w를 왕복 몇 번 했는지 알 수 있다.

(p + t) // w = x 이동 거리
(p + t) // h = y 이동 거리

그러나 현재 좌표에서 +인지 -인지는 해당 이동거리가 짝수냐 홀수냐에 달려있다.
(왜인지 원리는 모름)

'''

a = (p + t) // w 