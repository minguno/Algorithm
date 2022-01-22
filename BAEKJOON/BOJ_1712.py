# 8단계 기본수학1 손익분기점
# 이익이 발생하는 지점을 찾는 문제

'''

FC = fixed costs
VC = vairable costs
P = price
Q = quantity produced

total cost = FC + (VC * Q)
revenue = P * Q

Find a break-even point where

revenue(R) = total cost(C)
P * Q = FC + (VC * Q)

손익분기점을 지나 최초로 흑자를 얻는 판매량(Q)을 출력하기
없을 경우 (즉 Q가 0 이하일 경우) -1 출력.

Q = FC / (P - VC)

그러나 문제에서 손익분기점을 잘못 정의내려 수익이 최초로 발생되는
판매수량을 구하라고 한다.

R > C
R - C > 0
판매량은 whole number만 되므로 그냥 1차이라고 지정한다.
R - C = 1
Q = (FC + 1) / (P - VC) 을 기반으로 구한다.

'''

import math

# 각 variable 들의 값을 공백을 기준으로 나뉘어 입력받는다
FC, VC, P = map(int, input().split())

# ZeroDivisionError 때문에 앞에 P == VC를 꼭 써줘야 한다
if P == VC or (FC + 1) / (P - VC) < 0:
    # 문제에서 지정한 대로
    print(-1)
else:
    # 소숫점일 수도 있으니 올림한 정수로 반올림하여 출력한다
    print(math.ceil((FC + 1) / (P - VC)))


'''
int()나 round()를 쓰지 않은 이유?

int()는 부동소수점을 날려버리고 몫만 출력하기 때문에 최초 이익 
발생 지점 정수값의 -1 값으로 출력된다.

round() 또한 0.5 아래이냐에 따라 버림을 하기 때문에 whole number로만
존재하는 판매량 Q는 break-even point에서 올림만 해야한다.

그렇기 때문에 의도한 값을 정확하게 출력하기 위해선

math.ceil(i): 올림
math.floor(i): 내림
math.trunc(i): 버림

이 있다.

또 추가로 round() 함수같은 경우 0.5 선택의 기로에서 짝수 > 홀수 우선순위로
올림이냐 내림이냐가 갈린다.
e.g.)
1.5 -> 2 출력
4.5 -> 4 출력

'''