# 괄호검사

for t in range(int(input())):
    s = input()
    stack = []
    sol = 1
    for i in s:
        if i == '(' or i == '{':
            stack.append(i)
        elif i == ')':
            if not stack:
                sol = 0
                break
            elif stack[-1] != '(':
                sol = 0
                break
            else:
                stack.pop()
        elif i == '}':
            if not stack:
                sol = 0
                break
            elif stack[-1] != '{':
                sol = 0
                break
            else:
                stack.pop()
    if stack:
        sol = 0
    print(f'#{t + 1} {sol}')