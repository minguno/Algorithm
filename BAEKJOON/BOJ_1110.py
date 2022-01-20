# 정수로 풀이
N = int(input())
num = N
cycle = 0

# 무한히 반복 (언제 끝날지 모르니까)
while 1:
    a = num // 10
    # 새로운 수의 10의 자리
    b = num % 10
    # 새로운 수의 1의 자리
    c = (a + b) % 10
    # 새로운 정수
    num = b * 10 + c

    cycle += 1
    if num == N:
        break

print(cycle)

