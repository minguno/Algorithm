# 학년과 성별로 묶어 최소 개수의 방으로 방 배정하는 프로그램을 짜기

import math

N, K = map(int, input().split())

boys, girls = [], []
for _ in range(N):
    sex, year = map(int, input().split())
    # 남학생일 때
    if sex:
        boys.append(year)
    # 여학생일 때    
    if not sex:
        girls.append(year)

total = 0

# 학년별로 나눠주기
for y in range(1, 7):
    total += math.ceil(boys.count(y) / K) + math.ceil(girls.count(y) / K)

print(total)