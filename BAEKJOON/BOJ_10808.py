# 알파벳 개수

# 소문자 알파벳 아스키코드 범위
a = list(range(97, 123))
dct = {}
for k, v in enumerate(a):
    dct[chr(v)] = 0

s = input()
for c in s:
    dct[c] += 1
sol = []
for v in dct.values():
    sol.append(v)

print(*sol)