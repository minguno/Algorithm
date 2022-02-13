# 제로

stack = []
for _ in range(int(input())):
    n = int(input())
    if n != 0:
        stack.append(n)
    else:
        stack.pop()

total = 0
for i in stack:
    total += i
print(total)