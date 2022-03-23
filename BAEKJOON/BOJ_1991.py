# 트리 순회

def preord(v):
    global s1
    if v:
        s1 += char[v]
        preord(left[v])
        preord(right[v])


def inord(v):
    global s2
    if v:
        inord(left[v])
        s2 += char[v]
        inord(right[v])


def postord(v):
    global s3
    if v:
        postord(left[v])
        postord(right[v])
        s3 += char[v]


N = int(input())
char = [0] * (N + 1)
left = [0] * (N + 1)
right = [0] * (N + 1)
for _ in range(N):
    V, L, R = input().split()
    i = ord(V) - 64
    char[i] = V
    if L.isalpha():
        left[i] = ord(L) - 64
    if R.isalpha():
        right[i] = ord(R) - 64
sol = []
s1, s2, s3 = '', '', ''
preord(1)
inord(1)
postord(1)
sol.append(s1)
sol.append(s2)
sol.append(s3)
print(*sol, sep='\n')

