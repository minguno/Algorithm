# 종이자르기

w, h = map(int, input().split())

row, column = [0, h], [0, w]
for _ in range(int(input())):
    col, n = map(int, input().split())
    if col:
        column.append(n)
    else:
        row.append(n)
row.sort()
column.sort()

# 모든 가능한 w, h 구하기
width, height = [], []
# 원소끼리의 차를 구하는거라 len()보다 1 적기 때문에 range에서 -1
for i in range(len(row) - 1):
    height.append(row[i + 1] - row[i])
for i in range(len(column) - 1):
    width.append(column[i + 1] - column[i])

print(max(width) * max(height))

'''
처음에는

total = [[1 for _ in range(w)] for _ in range(h)]

총 면적을 2차원 배열로 생성해 row, column 값을 인덱스 값으로 
total을 slicing 해서 sum()을 통해 각 사각형의 면적을 areas 리스트에 넣어 
max(area)로 뽑아내려 함 (넘 복잡시러워서 포기)

0부터 n, n부터 h 식의 slicing 값을 추리다 width, height 접근 발견

'''