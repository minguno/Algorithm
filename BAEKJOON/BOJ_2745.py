# 진법 변환
# 문제에서 제시해준 것과 파이썬 시스템 설정이 동일
# A ~ Z 값이 10 ~ 35로 입력되어 있음

N, B = input().split()
# int 함수의 두 번째 인자는 n진법으로 바꿔준다
# default가 10진법
sol = int(N, int(B))
print(sol)