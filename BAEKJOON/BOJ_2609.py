# 최대공약수와 최소공배수

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

A, B = map(int, input().split())
print(gcd(A, B))
print(lcm(A, B))

'''
math 모듈을 사용하면 math.gcd로 최대공약수로, math.lcm으로 최소공배수 반환

'''
