N = int(input())

total = 0
for i in range(len(str(N))):
    total += N % 10
    N //= 10

print(total)

'''
처음 짠 코드

# 첫 번째
#입력받는 자연수 N
N = input()

if len(N) == 1:
    print(f'{int(N)}')
elif len(N) == 2:
    print(f'{int(N[0]) + int(N[1])}')
elif len(N) == 3:
    print(f'{int(N[0]) + int(N[1]) + int(N[2])}')
elif len(N) == 4:
    print(f'{int(N[0]) + int(N[1]) + int(N[2]) + int(N[3])}')
else:
    pass

=> 입력받는 숫자의 자릿수에 따라 조건문을 따로 작성해줬다

# 두 번째
# 입력받은 자연수 N
N = int(input())
sum = 0

# N은 최대 9999까지라 4자릿수
for i in range(0, 4):
    # 자연수가 아닐 때 실행하지 않는 제약
    if N <= 0:
        break;
    # 1의 자리 j
    j = N % 10
    # 자릿수를 줄인 다음 N에 assign; 다음 반복에 10의 자리가 1의 자리가 됨
    N = int(N / 10)
    # 계속 만들어낸 1의 자릿수를 sum에 더하기
    sum = sum + j

print(sum)

=> 제약 사항이란 입력값에 대해 주어진거라 코드에 따로 걸 필요가 없다
=> 코드 구현은 똑같으나 += 혹은 //= 사용 등 최종이 훨씬 간결해졌다

'''
