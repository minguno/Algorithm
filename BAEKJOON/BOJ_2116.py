# 주사위 쌓기
# 맨 처음 주사위의 윗면이 무엇이냐가 관건 -> 경우의 수 6개


from sys import stdin, stdout

reader = stdin.readline
writer = stdout.write

# (cnt - 1)번째 주사위 윗면의 숫자 top이 정해졌을 때 다음에 놓일 
# cnt번째 주사위의 아랫면을 지정하고 옆면의 최댓값을 뽑아내는 함수 정의
def get_max(cnt, top):
    numbers = list(range(1, 7))
    # 이전 주사위의 top은 이번 주사위의 아랫면 bottom
    bottom = top
    # 이번 주사위의 die pair의 value 값의 인덱스에 위치한 값 
    top = die_list[cnt][die_pair[die_list[cnt].index(bottom)]]
    numbers.remove(bottom)
    numbers.remove(top)
    return max(numbers)

# 각 입력값의 인덱스를 key로, 마주보는 주사위 값의 인덱스를 value로
# 리스트 형태로 [5, 3, 4, 1, 2, 0]의 인덱스 값을 뽑아쓰는 것도 가능
die_pair = {
    0: 5,
    1: 3,
    2: 4,
    3: 1,
    4: 2,
    5: 0
}

# 주사위 갯수
N = int(reader())

die_list = []
for _ in range(N):
    # 주사위 한 전개도 당 리스트로 묶어 2차원 배열로 받기
    die_list.append(list(map(int, reader().split())))


# 경우의 수 만큼 돌려본 옆면의 최댓값들의 합을 담을 리스트 생성
possible_sides = []

# 첫번째 주사위의 아랫면이 될 수 있는 경우의 수 6개에 대해 반복문 돌려보기
for bottom in range(1, 7):
    # 주사위 번째를 셀 변수 (인덱스 값이라 0부터 카운트)
    cnt = 0
    # 옆면의 최댓값을 누적합할 변수
    side = 0
    # 입력된 주사위를 다 훑을 때 까지
    while cnt < N:
        # bottom에 대한 top
        top = die_list[cnt][die_pair[die_list[cnt].index(bottom)]]
        side += get_max(cnt, top)
        # cnt + 1번째 주사위가 이어받을 아랫면의 수 지정하기
        bottom = top
        cnt += 1
    possible_sides.append(side)

# write 메서드는 문자열만 출력가능해서 변환해주기
writer(str(max(possible_sides)))