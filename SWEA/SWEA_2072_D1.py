# test case의 개수
N = int(input())

# 입력된 test case 수 만큼 반복되는 전체 작업
for i in range(N):

    # 입력받은 수를 공백 기준으로 분리해서 각각 숫자로 치환 후 리스트로 자료형 지정
    numbers = list(map(int, input().split()))
    odd_total = 0

    # numbers를 순회하면서
    for num in numbers:

        # 홀수만 하나씩 꺼내어 새 변수에 저장
        if num % 2 == 1:
            odd_total += num

    print("#{0} {1}".format(i + 1, odd_total))