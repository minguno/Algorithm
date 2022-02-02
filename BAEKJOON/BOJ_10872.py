# 10단계 재귀 팩토리얼

def factorial(N):
    # break point 지정해주기
    # N == 0일 때를 포함하기 위해 N == 1이 아닌 N <= 1로 해준다
    if N <= 1:
        return 1
    return N * factorial(N - 1)

print(factorial(int(input())))


'''
for문으로 팩토리얼 구현하기

N = int(input())

for i in range(1, N):
    N *= i

if N == (0 or 1):
    print(1)
else:
    print(N)


while문으로 팩토리얼 구현하기

N = int(input())

factorial = 1
while N > 1:
    factorial *= N
    N -= 1

print(factorial)

'''