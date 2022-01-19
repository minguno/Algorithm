# 입력받는 test case 횟수
T = int(input())
# 1-12월의 일수를 순서대로 담은 리스트
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# T만큼 반복되는 작업
for i in range(1, T + 1):
    date = input()
    # 편의를 위한 변수 지정
    year = int(date[0:4])
    month = int(date[4:6])
    day = int(date[6:8])
    # 날짜가 유효하던 안하던 상관 없기 때문에 번호 출력문은 조건문 밖에 & 일렬로 나올 수 있게 \n 날려주기
    print('#{} '.format(i), end='')
    # 2월 29일 윤년 조건 추가
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        month_days[1] = 29
    # month가 01-12 이내가 아닌 경우
    if month <= 0 or month >= 13:
        print(-1)
    # month가 범위 내일 경우
    else:
        # 31일 월수인 경우
        if month == (1 or 3 or 5 or 7 or 8 or 10 or 12):
            if day > 0 or day < 32 :
                print('{:04d}/{:02d}/{:02d}'.format(year, month, day))
            # day가 01-31 범위 밖인 경우
            else:
                print(-1)
        # 31일 월수가 아닌, 즉 2월이거나 나머지 월인 경우
        else:
            # 2월인 경우
            if month == 2:
                # month_days[1]인 이유는 윤년 조건을 달았기 때문
                if (day > 0) and (day <= month_days[1]):
                    print('{:04d}/{:02d}/{:02d}'.format(year, month, day))
                # 2월인데 day가 범위 밖인 경우
                else:
                    print(-1)
            # 30일 월수인 경우
            else:
                if (day > 0) and (day < 31):
                    print('{:04d}/{:02d}/{:02d}'.format(year, month, day))
                # day가 01-30 범위 밖인 경우
                else:
                    print(-1)

#
# # 윤년 조건 없이:
# for i in range(1, T + 1):
#     date = input()
#     # 편의를 위한 변수 지정
#     year = int(date[0:4])
#     month = int(date[4:6])
#     day = int(date[6:8])
#     print('#{} '.format(i), end='')
#     if month <= 0 or month >= 13:
#         print(-1)
#     else:
#         if month == (1 or 3 or 5 or 7 or 8 or 10 or 12):
#             if day > 0 or day < 32 :
#                 print('{:04d}/{:02d}/{:02d}'.format(year, month, day))
#             else:
#                 print(-1)
#         else:
#             if month == 2:
#                 if (day > 0) and (day <= 28):
#                     print('{:04d}/{:02d}/{:02d}'.format(year, month, day))
#                 else:
#                     print(-1)
#             else:
#                 if (day > 0) and (day < 31):
#                     print('{:04d}/{:02d}/{:02d}'.format(year, month, day))
#                 else:
#                     print(-1)