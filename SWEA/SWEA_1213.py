# String

# 방법 1 - 교수님
def check(s, M):
    for i in range(M):
        if src[s + i] != tar[i]:
            return False
    return True

for t in range(10):
    _ = input()
    tar = input()
    src = input()
    sol = 0
    for i in range(len(src) - len(tar) + 1):
        if check(i, len(tar)):
            sol += 1
    print(f'#{t + 1} {sol}')


# 내가 구현한 방법 2
# for문 돌려서 일치하는 첫 글자 나오면 전체 확인하기
for _ in range(10):
    t = int(input())
    target = input()
    sentence = input()
    sol = 0
    # len(target)
    M = 0
    for _ in target:
        M += 1
    # len(sentence)
    N = 0
    for _ in sentence:
        N += 1
    # sentence 캐릭터 중 target 첫 글자와 같은 글자가 나오면
    for i in range(N - M + 1):
        if sentence[i] == target[0]:
            # target 길이만큼의 뒷 자리를 비교하기
            if sentence[i:i+M] == target:
                sol += 1

    print(f'#{t} {sol}')

'''
# count() 메서드 활용

for _ in range(10):
    t = int(input())
    p = input()
    s = input()

    sol = s.count(p)
    print(f'#{t} {sol}')

'''