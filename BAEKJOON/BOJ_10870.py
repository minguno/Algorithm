# 10단계 재귀 피보나치 수

def fibb(N):
    fib0, fib1 = 0, 1
    if N <2:
        return N
    else:
        return fibb(N - 1) + fibb(N - 2)

print(fibb(int(input())))


'''
for문으로 피보나치 수 구하기

fib0, fib1 = 0, 1
for i in range(2, int(input()) + 1):
    fib2 = fib0 + fib1
    fib0, fib1 = fib1, fib2

print(fib2)


while문으로 피보나치 수 구하기

N = int(input())

if N < 2:
    print(N)
else:
    fib0, fib1 = 0, 1
    i = 2
    while i <= N:
        fib2 = fib0 + fib1
        fib0, fib1 = fib1, fib2
        i += 1
    print(fib2)

'''