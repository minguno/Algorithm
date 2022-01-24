# 8단계 기본 수학1 달팽이 올라가기
# 달팽이의 움직임을 계산하는 문제

'''
# 시간 초과로 백준 통과 못한 풀이:

# 입력값
A, B, V = map(int, input().split())

# 일 수를 세는 변수
days = 1

# 달팽이가 올라간 거리를 저장하는 변수
distance = 0

# True일 동안 무한히 반복
while 1:
    # 낮에 달팽이가 올라간 거리
    distance += A
    
    # 멈추는 조건문
    # 꼭대기 V에 도달했거나 넘었다면 반복문을 멈춘다
    if distance >= V:
        break
    
    # 꼭대기에 닿지 않았다면 밤동안 다시 미끄러져 distance가 줄어든다
    distance -= B
    
    # 낮 밤이 다 지나면 다음날 다시 오르므로 하루가 추가된다
    days += 1

print(days)

==> 혹은 distance 변수 없이 바로 V에서 A를 빼준 다음 0보다 작거나 같을 때
반복문을 중지시키는 코드도 짤 수 있다

'''

import sys
import math

A, B, V = map(int, sys.stdin.readline().split())

day = (V - B) / (A - B)

print(math.ceil(day))

'''
공식을 풀이해보자!

하루치 달팽이가 움직인 거리를 묶어준다 = A - B

그러나 V를 한번 지나치면 B는 실행되지 않는데, V / (A - B)는 이 조건을 포함하지 않는다
그렇기 때문에 애초에 V를 A가 넘겼을 때 B만큼 흘러내리는 일이 없도록
기둥의 거리를 줄여주는 (V - B) / (A - B) 방식으로 최소 일수를 구한다.

만약 소숫점이라면, 하루는 whole number로만 존재하기 때문에 +1 올림 해줘야 해서
math.ceil() method를 적용해준다.

'''