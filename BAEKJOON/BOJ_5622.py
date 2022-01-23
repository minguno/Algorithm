# 7단계 문자열 다이얼

'''
3의 배수로 늘어나는 아스키코드로 3배수 묶음시켜 알파벳 묶음을 일일히 치지 않아도 되나 싶었지만,
7번에 PQRS랑 WXYZ에 4씩 증가하는 변수가 있으므로, 이 방법이 더 꼬임.
'''

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

# 할머니가 입력한 알파벳
S = input()

# 최소 시간 누적합할 변수
time = 0

# 문자 하나씩 호출
for char in S:
    # 알파벳 인덱스 값에서
    for idx in range(len(dial)):
        # 해당 범위에 속해있는 문자라면
        if char in dial[idx]:
            # 1까지 2초 걸려서 +2와 인덱스 값이 0부터 시작이라 +1 고로 총 +3
            time += idx + 3

print(time)