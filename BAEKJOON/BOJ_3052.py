numbers = []
for i in range(10):
    n = int(input())
    numbers.append(n)

for num in numbers:
    remainder = [x % 42 for x in numbers]

print(len(set(remainder)))