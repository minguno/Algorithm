# 숨바꼭질 6
# 최대공약수 찾기

def gcd(a, b):
    a, b = min(a, b), max(a, b)
    while b > 0:
        a, b = b, a % b
    return a


N, S = map(int, input().split())
lst = list(map(int, input().split()))
diff = [abs(S - x) for x in lst]
sol = diff[0]
for i in range(N):
    sol = gcd(sol, diff[i])
print(sol)