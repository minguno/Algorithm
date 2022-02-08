# 일곱 난쟁이


from itertools import combinations


dwarfs = []
for _ in range(9):
    dwarfs.append(int(input()))

for i in list(combinations(dwarfs, 7)):
    if sum(i) == 100:
        dwarfs = list(i)
        break

dwarfs.sort()
print(*dwarfs, sep='\n')

'''
다른 풀이

import random

dwarfs = [int(input()) for _ in range(9)]
while 1:
    sample = random.sample(dwarfs, 7)
    if sum(sample) == 100:
        for i in sorted(sample):
            print(i)
        break

'''