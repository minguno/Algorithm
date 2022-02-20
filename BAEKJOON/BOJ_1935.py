# 후위 표기식2
# 피연산자는 값이 중복되지 않는다 -> 인덱스 카운터 활용

def Postfix(s):
    global lst
    stack = []
    for i in s:
        if 'A' <= i <= 'Z':
            stack.append(lst[ord(i) - ord('A')])
        else:
            str1 = stack.pop()
            str2 = stack.pop()
            if i == '+':
                stack.append(str2 + str1)
            elif i == '-':
                stack.append(str2 - str1)
            elif i == '*':
                stack.append(str2 * str1)
            else:
                stack.append(str2 / str1)

    return stack[0]


N = int(input())
s = input()
lst = [0 for _ in range(N)]
for i in range(N):
    lst[i] = int(input())

print(f'{Postfix(s):.2f}')

