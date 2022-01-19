# test case의 개수
T = int(input())

# 반복되는 횟수 겸 출력 번호 i
for i in range(1, T + 1):
    # 공백을 기준으로 구분하는 정수 리스트 생성
    numbers = list(map(int, input().split()))
    if numbers[0] > numbers[1]:
        print('#{} >'.format(i))
    elif numbers[0] == numbers[1]:
        print('#{} ='.format(i))
    else:
        print('#{} <'.format(i))