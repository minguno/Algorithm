number = int(input())
L = []

for i in range(1, number+1):
    if (number % i == 0):
        print("%d(은)는 %d의 약수입니다." % (i, number))
        L.append(i)
        if (len(L) == 2):
            print("%d(은)는 %d과 %d로만 나눌 수 있는 소수입니다." % (number, L[0], L[1]))