# 7단계 문자열
# 숫자를 뒤집어서 비교하는 문제

# 공백을 기준으로 입력받을 두 수
A, B = input().split()

#[::-1]로 인덱싱하면 문자열이 거꾸로 출력된다
if int(A[::-1]) > int(B[::-1]):
    print(A[::-1])
else:
    print(B[::-1])

'''
다른 방법도 있다

뒤집은 문자열을 저장할 공백 문자열을 생성하고
reverse_A = ''
reverse_B = ''

인덱스로 사용할 i에 대하여 끝부터 처음 값을 불러오는 range를 설정해준다
range(-1, 1, 1)로 써도 무방하다
for i in range(2, -1, -1):
    reverse_A += A[i]
    reverse_B += B[i]

if int(reverse_A) > int(reverse_B):
    print(reverse_A)
else:
    print(reverse_B)

'''