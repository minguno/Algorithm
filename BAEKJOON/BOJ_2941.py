# 7단계 문자열
# 크로아티아 알파벳의 개수를 세는 문제

# 입력받을 단어
# 제공되지 않은 운영체제로 변경해서 사용한 크로아티아 알파벳 값
encrypted_word = input()

special = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for char in special:
    # 해당 문자열이 존재하면 길이가 1인 아무 임의의 string으로 대체하는
    # .replace() 함수를 써 원래 알파벳과 길이수를 맞춰준다
    encrypted_word = encrypted_word.replace(char, '_')

print(len(encrypted_word))

'''
아래는 내가 처음 코드 짠 방식..

# 입력받을 단어
# 제공되지 않은 운영체제로 변경해서 사용한 크로아티아 알파벳 값
encrypted_word = input()

special = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# 원래 크로아티아 알파벳의 개수를 담을 변수
original_word_length = len(encrypted_word)

# 특수 문자를 담아놓은 리스트의 원소를 하나씩 호출해서
for char in special:        
    # 입력된 단어에 포함되어 있으면
    if char in encrypted_word:
        # 존재한 빈도수만큼 총 단어 길이에서 차감 해준다
        original_word_length -= encrypted_word.count(char)    

print(original_word_length)


=> 코드 설명

'dz='의 경우 혼자만 1번 있을 때 마다 단어 길이가 -2씩 감소한다

나머지는 1번 있을 때 마다 -1씩 단어 길이를 감소해야 하므로

따로 조건문을 걸어야 하나, 'z='가 'dz='에 포함되어 있으므로 .count()함수에 'dz=' 횟수와 중첩된다

고로 'dz=' 출현마다 -2 한 다음 중첩 카운트될 'z='에 대해 + 1 해주면 결국 총 감소값은 -1, 다른 원소들과 같다

때문에 따로 조건문을 걸 필요가 없다

'''