# 입력받을 단어
# 문제 상에서 대소문자가 상관없다고 했고, set 처리를 할 때 대소문자가 구분되니 통일시켜준다
# lower()도 무관하나 출력 예시가 모두 대문자라 나중에 출력할 때 .upper()를 추가해야되니 처음부터 capitalize하자
word = input().upper()

# 출연 횟수를 담을 list
count_list = []

# 중복값을 제거해줘서 count_list가 인덱스 역할을 할 수 있게 해준다
unique_char = set(word)

# 소문자로 일관되고 중복이 제거된 알파벳 하나씩 호출하여
for char in unique_char:
    # 주어진 단어 word에서 출현 횟수를 저장하여
    count = word.count(char)
    # 해당 문자를 unique_char에서 출력하기 위한 인덱스 값을 불러올 list에 저장해준다
    # 이는 .append()가 리스트 마지막에 원소를 추가해 unique_words set의 문자순대로 저장되서 가능한 method이다
    count_list.append(count)

# 빈도수가 가장 높은 수 max(count_list)가 count_list 내에 2개 이상이라면
if count_list.count(max(count_list)) >= 2:
    # 문제에서 제시한 대로 물음표를 출력하게 한다
    print('?')

# 그렇지 않다면
# .index() 함수를 사용하여 parameter로 주어진 빈도수가 가장 높은 수의 인덱스를 unique_char의 인덱스 값으로
# 받아 상응하는 알파벳을 출력한다
else:
    print(list(unique_char)[count_list.index(max(count_list))])

'''
여기서 else 문은 생략하면 안된다. Mississipi의 경우 ? 다음줄에 I가 출력되기 때문.
'''