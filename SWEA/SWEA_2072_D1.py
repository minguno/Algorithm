import math

# test case 입력받은 수
T = int(input())

# T만큼 반복되는 작업
for i in range(1, T + 1):
    # 입력 받은 10개의 스트링을 공백 기준으로 나눠 정수화 한 다음 리스트에 넣기
    numbers = list(map(int, input().split()))
    # 평균을 담을 변수 생성
    mean = round(sum(numbers) / len(numbers))
    print('#{} {}'.format(i, mean))