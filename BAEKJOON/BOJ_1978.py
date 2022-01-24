# 9단계 기본 수학2 소수 찾기
# 2부터 X-1까지 모두 나눠서 X가 소수인지 판별하는 문제 1

N = int(input())

# 리스트에 원소로 집어넣은 정수들
L = list(map(int, input().split()))

# 방법 1
count = 0

for i in L:
    if i < 2:
        continue
    for j in range(2, i):
        if not i % j: break
    else: count += 1

print(count)


# 혹은,

# 방법 2

count = sum(map(lambda x: all(x % j for j in range(2, x)) and x > 1, L))

print(count)

'''
Implications...

1. all()은 모든 값이 True일 때만 True를 반환한다

=> j가 x의 약수여서 나머지가 0이 된다면, x % j = 0 = False 이므로
   해당 수 x는 False로 반환된다

=> L의 원소가 해당 범위 안에 약수가 있다면 False로 없다면 True로 반환된다  

2. map(a, b)은 반복 가능한 객체 b에 함수 a를 적용해 object로 반환한다

=> sum() 함수는 boolean 값에 대해 true의 개수를 반환한다

'''