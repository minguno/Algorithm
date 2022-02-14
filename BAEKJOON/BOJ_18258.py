# 큐2
# contributor 노용래

# circular Queue 클래스 정의
class cirQueue():

    def __init__(self, N):
        self.N = N
        self.Q = [0 for _ in range(N)]
        # 초기 공백 상태엔 front = rear = 0
        self.front = 0
        self.rear = 0
        # queue 안에 또한 공백이라 0개의 원소
        self.size = 0

    def empty(self):
        if self.front == self.rear:
            return 1
        return 0
    
    def full(self):
        if (self.rear + 1) % self.N == self.front:
            return 1
        return 0

    def push(self, n: int):
        # 해당 문제에선 필요 없음
        # if self.full():
        #     return -1
        self.rear = (self.rear + 1) % self.N
        self.Q[self.rear] = n
        self.size += 1

    def pop(self):
        if self.empty():
            return -1
        # 공백/포화 상태 구분을 위해 0을 비워놓기 때문에
        # 1칸 넘어가서 출력한다
        self.front = (self.front + 1) % self.N
        temp = self.Q[self.front]
        self.size -= 1
        return temp
    
    # 가장 앞에 정수 출력
    def f(self):
        if self.empty():
            return -1
        # 0을 비워놓기 때문
        return self.Q[(self.front + 1) % self.N]
    
    # 가장 뒤 정수 출력
    def b(self):
        if self.empty():
            return -1
        return self.Q[self.rear]

    def s(self):
        return self.size


from sys import stdin
input = stdin.readline

N = int(input())

# 클래스 인스턴스 생성
q = cirQueue(N)
result = []

for _ in range(N):
    # x는 리스트 형태로 받는다
    cmd, *x = input().split()
    if cmd == 'push':
        q.push(int(x[0]))
    elif cmd == 'pop':
        result.append(q.pop())
    elif cmd == 'front':
        result.append(q.f())
    elif cmd == 'back':
        result.append(q.b())
    elif cmd == 'empty':
        result.append(q.empty())
    elif cmd == 'size':
        result.append(q.s())
    
print(*result, sep='\n')
