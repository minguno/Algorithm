# 풀이 1
while 1:
    try:
        A, B = map(int, input().split())
        print(A + B)
    except:
        break

# 풀이 2
try:
    while 1:
        A, B = map(int, input().split())
        print(A + B)
except:
    exit()