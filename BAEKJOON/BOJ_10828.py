# 스택

from sys import stdin
input = stdin.readline

stack = []
for _ in range(int(input())):
    cmd, *num = input().split()

    # push
    if cmd == 'push':
        stack.append(num)
    
    # pop
    elif cmd == 'pop':
        if len(stack):
            print(*stack.pop())
        else:
            print(-1)
    
    # top
    elif cmd == 'top':
        if stack:
            print(*stack[-1])
        else:
            print(-1)
    
    # size
    elif cmd == 'size':
        print(len(stack))
    
    # empty
    elif cmd == 'empty':
        print(0 if stack else 1)

'''
num 변수는 있을 때도 있고 없을 때도 있기 때문에 asterisk 처리 해줬다.
이와 같은 경우, 입력값이 그냥 'empty' 일 때 cmd = 'empty'를 담고 num = []
공백 리스트를 담게된다.

'''