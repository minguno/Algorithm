number = int(input())

for i in range(1, number+1):
    if (number % i == 0):
        print("%d(은)는 %d의 약수입니다." % (i, number))