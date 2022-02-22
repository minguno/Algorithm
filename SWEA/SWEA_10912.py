# 외로운 문자

for t in range(int(input())):
    lst = [x for x in input()]
    lst.sort()
    stack = []
    sol = ''
    for i in lst:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    if not stack:
        sol = 'Good'
    else:
        for i in stack:
            sol += i
    print(f'#{t + 1} {sol}')