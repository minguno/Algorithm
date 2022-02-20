# 최소공배수

for _ in range(int(input())):
    A, B = map(int, input().split())
    AA, BB = A, B
    while BB > 0:
        AA, BB = BB, AA % BB
    print(A * B // AA)