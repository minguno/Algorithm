# 입력받는 자연수 N
N = input()

if len(N) == 1:
    print(f'{int(N)}')
elif len(N) == 2:
    print(f'{int(N[0]) + int(N[1])}')
elif len(N) == 3:
    print(f'{int(N[0]) + int(N[1]) + int(N[2])}')
elif len(N) == 4:
    print(f'{int(N[0]) + int(N[1]) + int(N[2]) + int(N[3])}')
else:
    pass