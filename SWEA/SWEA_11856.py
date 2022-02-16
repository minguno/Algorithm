# 반반

for t in range(int(input())):
    word = input()
    l1 = []
    l2 = []
    sol = 'Yes'
    # 캐릭터 한개씩 리스트에 넣기
    for i in range(4):
        l1.append(word[i])
    for i in range(3):
        for j in range(i + 1, 4):
            if l1[i] == l1[j]:
                if l1[i] in l2:
                    continue
                l2.append(l1[i])
                l2.append(l1[j])
    # stack 원소 개수 계산
    cnt = 0
    for n in l2:
        cnt += 1
    if cnt < 4:
        sol = 'No'
    print(f'#{t + 1} {sol}')
