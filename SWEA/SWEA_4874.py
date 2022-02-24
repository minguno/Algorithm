# Stack2 Forth

for t in range(int(input())):
    s = input().split()[:-1]
    sol = 'error'
    stk = []
    for i in s:
        if i.isdigit():
            stk.append(int(i))
        else:
            try:
                n2 = stk.pop()
                n1 = stk.pop()

                if i == '+':
                    stk.append(n1 + n2)
                elif i == '-':
                    stk.append(n1 - n2)
                elif i == '*':
                    stk.append(n1 * n2)
                elif i == '/':
                    stk.append(n1 // n2)
            except:
                break

    if len(stk) == 1:
        sol = stk.pop()

    print(f'#{t + 1} {sol}')