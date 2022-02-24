# 반복문자 지우기

for t in range(int(input())):
    s = input()
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    print(f'#{t + 1} {len(stack)}')