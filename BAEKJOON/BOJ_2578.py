# 빙고

'''
빙고줄을 세는 구현을 하다 어떻게하면 이미 카운트 된 빙고줄이 다음에 누적되지 않을까? 에서 막혔다.

-> 이미 빙고줄을 센 원소들의 인덱스값을 리스트로 저장해서 not in 일 때만 더해주면?
    => 코드 길이가 상당히 귀찮아질 것 같다 인덱스 시렁..

-> 줄이 완성될 때마다 카운트 변수에 += 1 해주는게 아니라 번호가 호출될 때 마다 가로줄, 세로줄, 대각선을
   다 세서 3개 이상일 때 반복문을 멈추고 마지막으로 호출된 mc 번호의 index 값 + 1을 호출해주면?
    => 빙고줄을 세는 check 함수를 만들어야 할 듯 (2차원 배열 리스트를 그냥 for문에서 lambda 로 안추려진다)
    => T/F counter 리스트를 가로, 세로, 대각선으로 따로 만들어주면?
        => row_counter = [[1행][2행][3헹][][]]
        => column_counter = [[1열][2열]]
        => diag_counter = [[up][down]]
        해서 이들의 True 합이 3이상일 때

'''

from sys import stdin, stdout

reader = stdin.readline
writer = stdout.write


check = [[False for _ in range(5)] for _ in range(5)]
row_counter = [False] * 5
col_counter = [False] * 5
diag_counter = [False] * 2

# 번호가 불려서 해당 위치에 check에 True로 마크 될 때 마다 호출될 완성줄 확인함수
def check_bingo():
    # row
    for i in range(5):
        if all(check[i]):
            row_counter[i] = True
    
    # column
    for i in range(5):
        L = []
        for j in range(5):
            L.append(check[j][i])
        if all(L):
            col_counter[i] = True

    # diagonal
    up = []; down = []
    for i in range(5):
        up.append(check[i][4-i])
        down.append(check[i][i])
    if all(up):
        diag_counter[0] = True
    if all(down):
        diag_counter[1] = True

# check_bingo 함수로 업데이트 된 counter 리스트들에 대해 빙고줄이 3개 이상인지 확인하는 함수
def count_bingo():
    count = sum(row_counter) + sum(col_counter) + sum(diag_counter)
    return count >= 3

# 철수의 빙고
bingo = []
for _ in range(5):
    bingo.append(list(map(int, reader().split())))

# 사회자가 순서대로 호출한 번호들
mc = []
for _ in range(5):
    mc.extend(list(map(int, reader().split())))        

for idx in range(25):
    # row idx
    r = None
    for i in range(5):
        if mc[idx] in bingo[i]:
            r = i
            break
    # col idx
    c = bingo[r].index(mc[idx])
    # 호출된 숫자 표시
    check[r][c] = True
    check_bingo()
    if count_bingo():
        writer(str(idx + 1))
        break