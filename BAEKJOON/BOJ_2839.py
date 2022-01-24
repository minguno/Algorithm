# 8단계 기본 수학1 설탕 봉지
# 5와 3을 최소 횟수로 합하여 N을 만드는 문제

sugar = int(input())

bag = 0

# 5의 배수를 중점으로 반복문을 돌린다
# if문으로 5의 배수일 시 5로만 나누게 한다
# 아닐 시 3씩 감소 ( = 3의 배수) 시키며 5의 배수를 만든다
# 설탕이 딱 떨어지지 않고 음수가 된다면 -1을 출력시킨다

while sugar >= 0:
    if sugar % 5 == 0:
        bag += sugar // 5
        print(bag)
        break
    sugar -= 3
    bag += 1

else:
    print(-1)
