# 참외밭

'''
밭 면적 = 큰 사각형 넓이 - 작은 사각형 넓이
sol = 밭 면적 * 면적당 참외 개수

큰 사각형의 width, height는 방향이 1회씩만 나온다
-> dir 리스트 내에서 count로 찾기
또한 작은 사각형의 width, height는 큰 사각형의 height기준 3 번째 후에 나온다
'''


n = int(input())
dir = []
leng = []
for _ in range(6):
    a, b = map(int, input().split())
    dir.append(a)
    leng.append(b)

for i in range(6):
    # 방향이 1회만 나온 인덱스 값
    if dir.count(dir[i]) == 1:
        k = (i + 1) % 6
        # i의 다음 방향도 1회만 나온다면 큰 사각형 찾음
        if dir.count(dir[k]) == 1:
            big_h = i
            big_w = k
            small_w = (i + 3) % 6
            small_h = (i + 4) % 6
            break

sol = (leng[big_w] * leng[big_h] - leng[small_w] * leng[small_h]) * n
print(sol)