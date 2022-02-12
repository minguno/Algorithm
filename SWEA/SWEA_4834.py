# 숫자 카드

T = int(input())
for t in range(T):
    N = int(input())
    lst = [int(x) for x in input()]

    # 최고항 찾기
    k = lst[0]
    for num in lst:
        if k < num:
            k = num

    # 카운터 생성
    count = [0] * (k + 1)
    for num in lst:
        count[num] += 1

    # count.index(max(count))
    idx = None
    # 최고 출현 카드 count[idx]
    cmax = 0
    for i in range(k + 1):
        # 카드 장수가 같을 때는 제일 큰 숫자를 출력해야 하니 < 말고 <= 처리
        if cmax <= count[i]:
            cmax = count[i]
            idx = i

    print(f'#{t + 1} {idx} {cmax}')