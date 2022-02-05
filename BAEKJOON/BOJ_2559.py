# 수열
# 처음 slicing 한 sum값에 앞 값을 빼고 뒷 값을 더해주기

N, K = map(int, input().split())

temp = list(map(int, input().split()))
sliced = sum(temp[:K])
sum_list = [sliced]

for i in range(N - K):
    sliced = sliced - temp[i] + temp[K + i]
    sum_list.append(sliced)

print(max(sum_list))


'''
시간 초과된 코드 (최대 범위가 100,000이라 for문에 sum을 하는 것 때문으로 추정)

# 리스트를 주어진 갯수만큼 slicing해서 sum() 리스트의 max() 구하기

N, K = map(int, input().split())

temperature = list(map(int, input().split()))

sliced = []
for i in range(N - K + 2):
    sliced.append(sum(temperature[i: i + K]))

print(max(sliced))

'''