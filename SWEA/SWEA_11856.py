# 반반

# 내가 한 방법 1
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


# 실행 시간이 더 빠른 방법 2
for t in range(1, int(input()) + 1):
    word = input()
    temp = {}
    for w in word:
        if w in temp:
            temp[w] += 1
        else:
            temp[w] = 1
 
    vals = list(temp.values())
    try:
        if vals[0] == vals[1] == 2:
            result = 'Yes'
        else:
            result ='No'
    # 원소가 1개만 있을 때 vals[1]는 인덱스 에러
    except IndexError:
        result = 'No'
         
    print(f'#{t}', result)