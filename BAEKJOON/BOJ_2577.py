A = int(input())
B = int(input())
C = int(input())

# 0-9 대조 숫자 range
for i in range(10):
    # 각 자릿수 빈도수를 셀 변수
    cnt = 0
    # 문자열로 변환해 한 글자 씩 호출
    for j in str(A * B * C):
        # 한 숫자당 문자열이 끝까지 돌면서
        if j == str(i):
            # 빈도수 누적
            cnt += 1
    # 누적된 값을 가진 cnt를 출력하려면 지역 스코프에서 출력해야 한다
    print(cnt)
