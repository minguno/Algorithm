# 접미사 배열
# 문자열의 대소비교가 가능한 점을 이용 (리스트 대소비교와 같은 원리)

# 셀렉션 소트 사용한 방법
s = input()
lst = []

for i in range(len(s)):
    lst.append(s[i:])

for i in range(len(lst) - 1):
    mini = i
    for j in range(i + 1, len(lst)):
        if lst[mini] > lst[j]:
            mini = j
    lst[i], lst[mini] = lst[mini], lst[i]

print(*lst, sep='\n')


# sorted() 함수 사용한 방법
s = input()
lst = []

for i in range(len(s)):
    lst.append(s[i:])

for i in sorted(lst):
    print(i)

