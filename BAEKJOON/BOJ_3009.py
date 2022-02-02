# 9단계 기본 수학2 네 번째 점
# 직사각형을 완성하는 문제

'''
# 주어질 세 개의 점의 좌표
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

if a[0] == b[0]:
    if a[1] == c[1]:
        print(c[0], b[1])
    elif b[1] == c[1]:
        print(c[0], a[1])
elif b[0] == c[0]:
    if b[1] == a[1]:
        print(a[0], c[1])
    elif c[1] == a[1]:
        print(a[0], b[1])
elif c[0] == a[0]:
    if c[1] == b[1]:
        print(b[0], a[1])
    elif a[1] == b[1]:
        print(b[0], b[1])
'''


# 그러나 이는 비트 연산자로 훨씬 간편한 코드를 짤 수 있다.

x = y = 0

# 3개의 좌표를 받는 작업을 반복
for _ in range(3):
    a, b = map(int, input().split())
    x ^= a
    y ^= b

print(x, y)

'''
XOR 비트 연산자 논리

비트가 서로 다르면 1, 같으면 0이 된다. 고로 아래의 성질을 같게 되는데,

1. 값이 0인 변수에 x값으로 ^= (XOR) 연산을 하면 그 변수는 x가 된다.

2. 값이 x인 변수에 z값으로 XOR 연산을 두 번 하면 원래의 값 x가 된다.
e.g.) 010101 ^ 001100 ^ 001100 = 010101

=> 고로 x, y 좌표에서 짝이 없는 수를 뽑아낼 수 있다.

'''