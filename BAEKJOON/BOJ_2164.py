# 카드2

from collections import deque

N = int(input())
Q = deque(list(range(1, N + 1)))

while N > 1:
    Q.popleft()
    Q.append(Q.popleft())
    N -= 1
print(*Q)


'''
모듈을 사용하지 않는 풀이
-> 실제로 어떤 메서드도 사용하지 않지만 인덱스 값 조작을 이용한 눈속임(?)

N = int(input())
Q = list(range(1, N + 1))
front = 0

while N > 1:
    # pop
    front += 1
    # front가 제일 마지막 인덱스라 다음 pop을 실행시킬 수 없을 때 loop 종료
    if front == len(Q) - 1:
        break
    Q.append(Q[front])
    # 두번째 pop 실행
    front += 1

print(Q[-1])

'''

'''
시간 초과

방법 1
-> pop()은 시간 복잡도가 O(1)인데에 반해 pop(x)는 O(n)만큼 걸려
시간초과가 났다

방법 2
-> [::-1]로 해도 리스트 자체값을 바꾼게 아니기 때문에 pop()은 
원래 리스트의 제일 뒤에 위치한 원소를 반환하면서, 리스트에서 
제거되지 않는다

N = n = int(input())
Q = list(range(1, N + 1))

# 방법 1
while n > 1:
    Q.pop(0)
    Q.append(Q.pop(0))
    n -= 1
print(*Q)

혹은

# 방법 2
while n > 1:
    Q[::-1].pop()
    Q.append(Q[::-1].pop())
    n -= 1

그에 반해 collections의 deque 모듈의 모든 메서드는 O(1)의 시간
복잡도를 소요해 시간 초과가 나지 않는다

'''