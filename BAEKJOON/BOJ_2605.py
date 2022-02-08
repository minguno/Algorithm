# 줄 세우기
'''
학생이 뽑는 번호를 인덱스로 삼아 학생 번호 i를 공백 리스트에 더해준다
문제는 맨 뒤를 기준점으로 잡아 학생을 추가하지만 insert() 메서드는 앞을 0 기준점으로
삼기 때문에 출력할 때 거꾸로 뒤집어준다

'''

n = int(input())
movement = list(map(int, input().split()))

i = 1
result = []
for m in movement:
    result.insert(m, i)
    i += 1

print(*result[::-1])