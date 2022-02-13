# 11단계 정렬

from sys import stdin
input = stdin.readline

N = int(input())

c = [0] * 10001
for _ in range(N):
    c[int(input())] += 1
for i in range(10001):
    if c[i] != 0:
        for j in range(c[i]):
            print(i)

'''
sys 모듈을 쓰지 않으면 시간 초과가 나오고,
temp 리스트로 정식 카운팅 정렬을 하면 메모리 초과가 나온다

'''