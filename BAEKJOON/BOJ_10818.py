# 방법 1. 내장 함수 사용
import math

N = int(input())
numbers = list(map(int, input().split()))
print('{} {}'.format(min(numbers), max(numbers)))

# 방법 2. 반복문 사용
N = int(input())
numbers = list(map(int, input().split()))
maximum, minimum = numbers[0], numbers[0]
for i in numbers:
    if maximum < i:
        maximum = i
    if minimum > i:
        minimum = i
print(f'{minimum} {maximum}')