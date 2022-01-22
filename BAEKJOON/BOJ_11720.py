# 입력받을 숫자의 개수
N = int(input())

# 공백없이 입력받을 N개의 숫자
number_str = input()

# N개의 숫자의 합을 담을 변수 생성
total = 0

# for문으로 문자열로 받은 N개의 수를 한개씩 떼어 total 변수에 누적하기
for number in number_str:
    total += int(number)

# N개의 숫자의 합인 total 출력
print(total)