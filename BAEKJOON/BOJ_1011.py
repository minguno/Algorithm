# 8단계 기본 수학1 Fly me to the Alpha Centauri
# 거리에 따른 장치 사용 횟수를 출력하는 문제

T = int(input())

for _ in range(T):
    departure, destination = map(int, input().split())
    distance = destination - departure - 1
    # 직전의 이동거리를 빼줬으니 카운트에 포함시켜준다
    count = 1
    while distance / 2 > 1:
        
        count += 2