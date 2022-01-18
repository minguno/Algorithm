# 3.14로는 출력값이 달라서 라이브러리 불러오기
from math import pi

# 리스트 내포 기능을 이용하여 콤마로 구분해 입력받은 리스트 생성
circumference = [2 * pi * int(i) for i in input().split(', ')]

# 부동소수점 자릿수 지정해주기
for j in circumference[: -1]:
    print("{:0.2f}".format(j), end=', ')
print("{:0.2f}".format(circumference[-1]))