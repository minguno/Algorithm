# 자리배정
# 공연장 크기가 주어졌을 때, K번째 관객이 배정될 좌석 번호(x, y) 반환하기

'''
달팽이 수열 문제
=> 한 방향으로 빙글빙글 채워지는 행렬

시작부터 한 면 당 좌석이
r - 0 개
c - 1 개
r - 1 개
c - 2 개
r - 2 개

방법 1.
증가하는 감소치를 for문으로 돌려 range를 설정한 뒤
해당 범위 안에 들어올 때 까지 while 문으로 돌려주기
=> 각 모서리 범위 (아찔...)

방법 2.
지정해준 방향대로 2차원 배열 grid를 생성해 1부터 순서대로 넣어주기
=> 규칙을 어떻게?
=> dx = [0, 1, 0, -1]; dy = [1, 0, -1, 0] 인덱스값으로 호출할 변수를 
   for range(4) 돌려서 한 바퀴 돌아서 안에 들어오면 다시 0부터?

'''
from sys import stdin, stdout
reader = stdin.readline
writer = stdout.write

c, r = map(int, reader().split())
n = int(reader())

# 예외 처리
if n > c * r:
    writer('0')
elif n <= r:
    writer(f'1, {n}')
else:
    # 시작 모서리값
    edge = r