# test case 개수
T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    print(f'#{i + 1} {a // b} {a % b}')
