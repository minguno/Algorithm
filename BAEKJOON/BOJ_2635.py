'''
규칙 찾기!

C0 = 100
C1
C2 = C0 - C1 = 100 - C1
C3 = -C0 + 2C1 = -100 + 2C1
C4 = 2C0 - 3C1 = 2 * 100 - 3C1
C5 = -3C0 + 5C1 = -3 * 100 + 5C1
C6 = 5C0 - 8C1 = 5 * 100 - 8C1
C7 = -8C0 + 13C1 = -8 * 100 + 13C1

는 개뿔. 그냥 문제에서 하란대로 하면 된다.

'''

C0 = int(input())
cnt = 0

for i in range(C0 + 1):
    # 임의의 두번째 수 i에 대해
    numbers = [C0, i]
    while 1:
        if numbers[-2] - numbers[-1] >= 0:
            numbers.append(numbers[-2] - numbers[-1])
        else:
            break
    # 수들의 개수의 최댓값을 저장하기
    if len(numbers) > cnt:
        cnt = len(numbers)
        minimum = numbers

print(cnt)
print(*minimum, sep=' ')