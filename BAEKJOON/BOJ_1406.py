# 에디터

from sys import stdin, stdout
rd = stdin.readline
wr = stdout.write

# 스택 활용
# 커서의 위치가 두 스택 사이점이 된다
# stack2는 LIFO 특성으로 뒤집어서 extend 처리

stack1 = list(rd().rstrip())
stack2 = []
for _ in range(int(rd())):
    cmd, *x = rd().split()
    if cmd == 'L':
        if stack1:
            stack2.append(stack1.pop())
    elif cmd == 'D':
        if stack2:
            stack1.append(stack2.pop())
    elif cmd == 'B':
        if stack1:
            stack1.pop()
    else:
        stack1.append(x[0])

stack1.extend(stack2[::-1])
print(''.join(stack1))





'''
# 시간 초과 (제한 0.3초)

class Editor():

    def __init__(self, lit):
        self.lit = lit
        self.N = len(self.lit)
        self.cur = self.N

    def L(self):
        if self.cur == 0:
            pass
        else:
            self.cur -= 1

    def D(self):
        if self.cur == self.N:
            pass
        else:
            self.cur += 1

    def B(self):
        if self.cur == 0:
            pass
        else:
            self.lst.pop(self.cur - 1)
            self.cur -= 1
            self.N -= 1

    def P(self, x: str):
        temp = self.lit[: self.cur]
        temp += x
        self.lst = temp + self.lit[self.cur:]
        self.cur += 1
        self.N += 1

    def W(self):
        wr(''.join(self.lst))

word = rd()[:-1]
word = Editor(word)
for _ in range(int(rd())):
    cmd, *x = input().split()
    if cmd == 'P':
        word.P(x[0])
    elif cmd == 'L':
        word.L()
    elif cmd == 'D':
        word.D()
    else:
        word.B()
word.W()
'''