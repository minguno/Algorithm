# 스택 균형잡힌 세상
# 괄호 심화

def is_vps(lit):
    stack = []
    for i in lit:
        # push
        if i == '(' or i == '[':
            stack.append(i)
        # pop for )
        elif i == ')':
            if len(stack) == 0:
                return 'no'
            else:
                temp = stack.pop()
                if temp != '(':
                    return 'no'
        # pop for ]
        elif i == ']':
            if len(stack) == 0:
                return 'no'
            else:
                temp = stack.pop()
                if temp == '(':
                    return 'no'
    # 짝이 딱 맞을 때
    if not len(stack):
        return 'yes'
    # 오른쪽 괄호가 왼쪽 괄호보다 적을 때
    return 'no'

while 1:
    lit = input()
    if lit == '.':
        break
    print(is_vps(lit))