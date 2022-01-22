# 한수의 개수를 세는 함수 정의하기
def count_hansoo(number):
    # 1-2자릿수 숫자들은 모두 한수이다
    if 1 <= N < 100:
        cnt = N
        return cnt
    # 세자릿수 숫자부터는 규칙이 생기기 때문에 이전의 한수들을 (1-99) 카운트하고 시작한다
    cnt = 99
    # 100 이상과 입력된 값의 범위 내의 숫자들을 문자열로 변환시켜 리스트로 저장한다
    # 각 숫자 문자열들을 꺼내 인덱스로 자릿수를 하나씩 불러와 다시 정수로 변환시킨다
    for num in list(map(str, range(100, N + 1))):
        # 첫 번째와 두 번째 자릿수의 차이와 두 번째와 세 번째 자릿수의 차이가 같다면, 등차수열을 이뤄 한수가 된다
        # 그럴 때 마다 cnt 변수가 1씩 증가한다
        if int(num[0]) - int(num[1]) == int(num[1]) - int(num[2]):
            cnt += 1
    # 위에 지역변수 cnt = 99를 지정해놨기 때문에 return 인덴트를 같은 스코프에 넣어야만 제대로 카운트한 값이 출력된다
    return cnt


N = int(input())

print(count_hansoo(N))