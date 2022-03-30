# 잃어버린 괄호

s = input().split('-')
N = len(s)
for i in range(N):
    s[i] = sum(map(int, s[i].split('+')))
sol = s[0]
N = len(s)
i = 1
while i < N:
    sol -= s[i]
    i += 1
print(sol)