# 스택 스택수열

N = int(input())
stack = []
signs = []
flag = True
n = 1
for i in range(N):
    num = int(input())
    while n <= num:
        stack.append(n)
        signs.append('+')
        n += 1
    if stack[-1] == num:
        stack.pop()
        signs.append('-')
    else:
        flag = False
for i in signs:
    if not flag:
        print('NO')
        break
    print(i)

'''
이 문제는 이해하는 것 자체가 오래 걸렸다. 입력문과 출력문의 관계를 찾는 것이.
기본적으로 1, 2, 3, ... n의 수에 대해 stack에 push와 pop을 선택적으로 써가며
pop() 한 수들이 입력받은 수들의 순서/수열과 같아야 한다.

그런데 입력받은 수와 stack에서 pop()하면 나올 수 (제일 마지막 원소) 가 같지 않다면,
stack으로 수열 생성이 불가능하단 것이므로 NO를 출력한다.
'''