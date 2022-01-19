# 입력받는 test case 횟수
T = int(input())
# 31일을 가진 월의 리스트
month_31 = [1, 3, 5, 7, 8, 10, 11]
# 30일을 가진 월의 리스트
month_30 = [4, 6, 9, 11]

# T만큼 반복되는 작업
for i in range(1, T + 1):
    date = input()
    if int(date[3:5]) == 02 and int(date[5:7]) <= 28:
