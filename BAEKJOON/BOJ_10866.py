# 덱

from sys import stdin
input = stdin.readline


class Deque():
    
    def __init__(self, N):
        # 총 덱의 길이
        self.N = N
        # 리스트 덱
        self.D = [0 for _ in range(N)]
        self.front = 0
        self.rear = 0
        # 보유한 원소 개수
        self.size = 0

    def push_f(self, x: int):
        self.D[self.front] = x
        # 앞으로 한 칸
        # 0 비우고 덱 맨 마지막 자리에 위치
        self.front = (self.front - 1 + self.N) % self.N
        self.size += 1
    
    def push_b(self, x: int):
        # 뒤로 한 칸
        self.rear = (self.rear + 1) % self.N
        self.D[self.rear] = x
        self.size += 1
    
    def pop_f(self):
        if self.empty():
            return -1
        # 뒤로 한 칸
        self.front = (self.front + 1) % self.N
        self.size -= 1
        return self.D[self.front]
    
    def pop_b(self):
        if self.empty():
            return -1
        # 먼저 구하고
        temp = self.D[self.rear]
        # 앞으로 한 칸
        self.rear = (self.rear - 1) % self.N
        self.size -= 1
        return temp
    
    def f(self):
        if self.empty():
            return -1
        return self.D[(self.front + 1) % self.N]
    
    def b(self):
        if self.empty():
            return -1
        return self.D[self.rear]

    
    def empty(self):
        if self.front == self.rear:
            return 1
        return 0
    
    def full(self):
        if self.size == self.N:
            return 1
        return 0
    
    def S(self):
        return self.size


N = int(input())
d = Deque(N)
ans = []
for _ in range(N):
    cmd, *x = input().split()
    if cmd == 'push_back':
        d.push_b(x[0])
    elif cmd == 'push_front':
        d.push_f(x[0])
    elif cmd == 'front':
        ans.append(d.f())
    elif cmd == 'back':
        ans.append(d.b())
    elif cmd == 'empty':
        ans.append(d.empty())
    elif cmd == 'size':
        ans.append(d.S())
    elif cmd == 'pop_front':
        ans.append(d.pop_f())
    elif cmd == 'pop_back':
        ans.append(d.pop_b())

print(*ans, sep='\n')

