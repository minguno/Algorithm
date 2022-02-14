# 단어 뒤집기
# 후입선출 LIFO 특성을 가진 스택 활용

from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    lst = list(input().split())
    stack = []
    result = []
    for i in range(len(lst)):
        temp = ''
        for j in range(len(lst[i])):
            stack.append(lst[i][j])
        for _ in range(len(stack)):
            temp += stack.pop()
        result.append(temp)
    
    print(*result)

