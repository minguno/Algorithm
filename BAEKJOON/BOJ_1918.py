# 후위 표기식

cal = input()
stck = []
sol = []
for c in cal:
    if c == '(':
        stck.append(c)
    elif c == ')':
        while stck:
            if stck[-1] == '(':
                stck.pop()
                break
            sol.append(stck.pop())
    elif c == '+' or c == '-':
        while stck:
            if stck[-1] == '(':
                break
            sol.append(stck.pop())
        stck.append(c)
    elif c == '*' or c == '/':
        while stck:
            if stck[-1] == '+' or stck[-1] == '-' or stck[-1] == '(':
                break
            sol.append(stck.pop())
        stck.append(c)
    else:
        sol.append(c)

while stck:
    sol.append(stck.pop())

print(''.join(sol))