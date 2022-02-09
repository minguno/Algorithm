# 수열
# 입력값 중 consecutive increase / decrease of numbers 찾아서 수열 구간 찾기
# 3, 4, 5, 5, 6 이 연속으로 나온 경우엔 구간의 길이가 len(range(3, 7)) = 4

n = int(input())
lst = list(map(int, input().split()))

# n = 1일 때 최대 수열 길이가 1이라
result = 1

cnt = 1
# increase
for i in range(1, n):
    if lst[i] >= lst[i - 1]:
        cnt += 1
        if result < cnt:
            result = cnt
    # reset
    else:
        cnt = 1

# reset
cnt = 1
for i in range(1, n):
    if lst[i] <= lst[i - 1]:
        cnt += 1
        if result < cnt:
            result = cnt
    # reset
    else:
        cnt = 1

print(result)

'''
이 문제에서 하나의 for 문으로 오름차순과 내림차순을 같이 
구분하려다 보니까 인덱스가 엄청 꼬이고 코드가 길어짐.

2개의 separate for문으로 돌리는 게 key!

'''