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
리스트에서 원소와 길이가 같다면 ==의 결과값이 True이다.
앞에서부터 같으면 같은 인덱스의 원소값이 달라질 때 > 혹은 < 적용된다.

원소 하나하나의 대소 관계나 특정 값에 대한 모든 원소의 관계 연산자 적용은
numpy.array(list)를 사용할 수 있다.

numpy.array(list) < list(A) 하면 
list 각 원소가 list(A) 원소보다 작은가에 대한 boolean 값 반환.

list < list(A) 하면
두 리스트의 첫 번째 원소부터 비교 연산을 하되, 두 원소의 값이 다를 때
연산을 끝까지 하지 않고 중단되며 해당 인덱스 원소에 대한 boolean 값 반환.
e.g.) L = [4, 3, 2, 1]와 A = [3, 3]이 있을 때
      L > A 는 True이다.
      => 0번째 원소에서 L이 더 크기 때문.

'''


'''
리스트 관계 연산자 사용에 대해 모르고 처음 짠 코드

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