# 8단계 기본 수학1 분수 찾기
# 분수의 순서에서 규칙을 찾는 문제

'''
번호가 메겨진 순서대로 대각선을 긋다보면
대각선 1번째 = 1/1
대각선 2번째 = 1/2, 2/1
대각선 3번째 = 3/1, 2/2, 1/3
대각선 4번째 = 1/4, 2/3, 3/2, 4/1
대각선 5번째 = 5/1, 4/2, 3/3, 2/4, 5/1

식으로 규칙을 찾을 수 있다.

홀수일 때는 numerator +1 씩 증가하고, denominator -1씩 감소
짝수일 때는 numerator -1 씩 감소하고, denominator +1씩 증가

또한 해당 범위는 range(1, 대각선 n번째 + 1) 안의 숫자들로만 분수가 이루어진다.
그리고 sum(range(1, 대각선 n번째 + 1)) 단위로 대각선 번째가 1씩 증가한다.
==> 2차원 리스트 배열이라고 이해하면 좀 더 쉽다.
line = [대각선 번째가 1씩 증가하는 리스트]
line = [[1], [2], [3], [4] ... [n]] => 분수 숫자 범위
line = [[1/1], [1/2, 2/1], [3/1, 2/2, 1/3], [1/4, 2/3, 3/2, 4/1] .. [*중요*]]

여기서 *중요*가 무엇일까?
n이 짝수라면 -> 1/n, 2/n-1, 3/n-2, ... , n-1/2, n/1
n이 홀수라면 -> n/1, n-1/2, n-2/3, ... , 2/n-1, 1/n

고로 주어진 범위를 찾으면 누적합만큼 빼주고, 차를 인덱스 범위로 활용해서
분수값을 도출할 수 있다.

만약 X = 8, 그럼 n은 4이다. idx = 2가 된다.
n은 짝수임으로, {top}은 1부터 시작하고 {bottom}은 n부터 시작한다.

list(range(1, n + 1)) 에서
[idx] 값이 top에, [-idx] 값이 bottom에 간다.

'''

X = int(input())

# 대각선 번째
n = 0

# n번째 대각선에 위치한 X번 분수 찾기
# 해당 범위보다 X가 작기 시작한 지점이 속한 대각선 번째이다
while X > sum(range(n + 1)):
    n += 1

# n - 1번째 대각선까지의 분수번호들을 빼줘서 인덱스값으로 호출할 수 있게 초기화해준다
# 인덱스는 0부터 시작이기 때문에 -1 해준다
idx = X - sum(range(n)) - 1

# 분수 숫자를 호출할 리스트 생성
L = list(range(1, n + 1))

# 끝부터 부르는 reverse index는 -1부터 시작이라 + 1 해준다
if n % 2 == 0:
    print(f'{L[idx]}/{L[-(idx + 1)]}')
else:
    print(f'{L[-(idx + 1)]}/{L[idx]}')