# 스택 오큰수


from sys import stdin
input = stdin.readline

N = int(input())
lst = list(map(int, input().split()))
stack = []
# default 값을 -1으로 설정
ans = [-1] * N

# i-1번째 값에 대해 i번째 값을 비교하기
for i in range(N):
    # stack이 공백일 땐 실행되지 X
    # i-1번째 값이 i번째 값보다 커도 실행 X
    while stack and stack[-1][0] < lst[i]:
        # i번째 값을 i-1번째 값의 인덱스에 지정
        ans[stack[-1][1]] = lst[i]
        # i-1번째 값을 없앤다
        stack.pop()
    # i-1번째 값 추가
    stack.append([lst[i], i])
print(*ans)

'''
N 최대 범위가 1,000,000이라 시간 초과되는 코드

N = int(input())
lst = list(map(int, input().split()))
ans = []
for i in range(N):
    for j in lst[i:]:
        if lst[i] < j:
            ans.append(j)
            break
        elif j == lst[-1]:
            ans.append(-1)

print(*ans)
'''