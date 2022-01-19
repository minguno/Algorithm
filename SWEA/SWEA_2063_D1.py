# 입력으로 받는 정수의 횟수
N = int(input())

# 공백을 기준으로 나눠받은 N개의 정수 리스트
L = list(map(int, input().split()))

# 오름차순 정렬
L.sort()

# 중앙값 변수 지정; 인덱스가 정수가 되기 위해 int()
median = L[int(N/2)]

# 출력
print(median)