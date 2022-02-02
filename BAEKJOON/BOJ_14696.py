# 딱지놀이

for _ in range(int(input())):
    # 슬라이싱으로 딱지 배열만 순서 정렬해준 리스트
    A = sorted(list(map(int, input().split()))[1:], reverse=True)
    B = sorted(list(map(int, input().split()))[1:], reverse=True)

    if A == B:
        print('D')
    elif A > B:
        print('A')
    else:
        print('B')

'''
N = int(input())

for _ in range(N):
    A = list(map(int, input().split()))[1:]
    B = list(map(int, input().split()))[1:]

    # 별
    if A.count(4) > B.count(4):
        print('A')
        continue
    elif A.count(4) < B.count(4):
        print('B')
        continue

    # 동그라미
    if A.count(3) > B.count(3):
        print('A')
        continue
    elif A.count(3) < B.count(3):
        print('B')
        continue

    # 네모
    if A.count(2) > B.count(2):
        print('A')
        continue
    elif A.count(2) < B.count(2):
        print('B')
        continue

    # 세모
    if A.count(1) > B.count(1):
        print('A')
        continue
    elif A.count(1) < B.count(1):
        print('B')
        continue
    
    #무승부
    print('D')
    '''