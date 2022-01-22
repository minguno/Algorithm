# 입력받을 test case 횟수
T = int(input())

# T만큼 반복되는 작업
for i in range(T):
    # 반복 횟수 R과 문자열 S를 공백 기준으로 입력받기
    R, S = input().split()
    
    # 각 문자가 반복된 문자열을 담을 변수 생성하기
    final = ''
    
    # 반복하기 위해 문자 하나씩 호출하기
    for char in S:        
        # 각 문자마다 R씩 반복하는 문자열로 변경하기
        char *= int(R)
        final += char

    # str.format을 사용하여 출력문 작성
    print(final)

'''
처음에는 str.format으로 계산문 자체를 변수로 넣을 생각이었어서 escapse sequence 출력에
아래와 같이 조건을 넣었다.

# escapse sequence도 입력될 수 있으므로, 입력과 동일하게 출력되도록 변환해준다
# if char == '\\':
#     char = '\\\\'

그런데 공백 문자열 final에 반복된 문자를 개별적으로 추가하고 일반 print 문으로 출력할거라
\ 입력해도 \ 그대로 입력되었다.

만약 str.format이었다면 어땠을지 나중에 시험해보고 싶다.

'''