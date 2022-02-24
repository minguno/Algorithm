# 토너먼트 카드게임

def solve(s, e):
    # 종료조건
    if s == e:
        return s
    # 좌, 우에서 승자 각각 구하기
    l = solve(s, (s + e) // 2)
    r = solve((s + e) // 2 + 1, e)
    # 최종 승자 리턴
    if (lst[l] + 1) % 3 == lst[r] % 3:
        return r
    else:
        return l


for t in range(int(input())):
    N = int(input())
    lst = [0] + list(map(int, input().split()))
    sol = solve(1, N)
    print(f'#{t + 1} {sol}')