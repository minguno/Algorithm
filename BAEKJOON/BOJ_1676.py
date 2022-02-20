# 팩토리얼 0의 개수
# 0의 개수는 10(2 * 5)이 곱해지는 순간 늘어나기 때문에 5의 개수를 찾는다
# i.e. 10!은 5에서 한 번, 10에서 한 번 0이 생기기 때문에 답이 2
# N범위가 500이하이기 때문. 625는 미포함

N = int(input())
print(N//5 + N//25 + N//125)

# n 팩토리얼을 계산한 뒤 str으로 바꾸고 뒤집어서 카운트하기
def fact(N):
    if N < 1:
        return 1
    return N * fact(N - 1)

n = int(input())
sol = 0
rev_nf = str(fact(n))[::-1]
for i in rev_nf:
    if int(i):
        break
    sol += 1
print(sol)