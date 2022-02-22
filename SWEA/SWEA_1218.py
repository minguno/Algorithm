# 괄호 짝짓기

for t in range(10):
    _ = int(input())
    s = input()
    stack = []
    sol = 1
    for i in s:
        if i == '(' or i == '{' or i == '[' or i == '<':
            stack.append(i)
        elif i == ')':
            if not stack:
                sol = 0
                break
            elif stack[-1] == '(':
                stack.pop()
            else:
                sol = 0
                break
        elif i == '}':
            if not stack:
                sol = 0
                break
            elif stack[-1] == '{':
                stack.pop()
            else:
                sol = 0
                break
        elif i == ']':
            if not stack:
                sol = 0
                break
            elif stack[-1] == '[':
                stack.pop()
            else:
                sol = 0
                break
        else:
            if not stack:
                sol = 0
                break
            elif stack[-1] == '<':
                stack.pop()
            else:
                sol = 0
                break
    if stack:
        sol = 0

    print(f'#{t + 1} {sol}')