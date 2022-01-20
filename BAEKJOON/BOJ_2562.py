import math

numbers = []

for i in range(9):
    n = int(input())
    numbers.append(n)

for j in range(len(numbers)):
    if max(numbers) == numbers[j]:
        location = j + 1

print(f'{max(numbers)}\n{location}')