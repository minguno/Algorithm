# 단어 뒤집기 2
sentence = input()

sol = []
stack = []
temp = ''
i = 0
while i != len(sentence) - 1:
    # 태그 추가
    if sentence[i] == '<':
        while sentence[i] != '>':
            temp += sentence[i]
            i += 1
        temp += sentence[i]
        if not i == len(sentence) - 1:
            i += 1
    
    # 공백일 때 뒤집은 단어 추가
    elif sentence[i] == ' ':
        sol.append(temp)
        temp = ''
        i += 1
    
    else:
        # 숫자나 알파벳 stack에 추가
        while sentence[i] != ' ' and sentence[i] != '<' and i != len(sentence) - 1:
            stack.append(sentence[i])
            if not i == len(sentence) - 1:
                i += 1
                if i == len(sentence) - 1:
                    stack.append(sentence[i])
        # LIFO로 temp에 추가
        while len(stack) != 0:
            temp += stack.pop()
    
    # i가 마지막 인덱스 값일 때 temp에 저장되어 있는 문자열 추가
    if i == len(sentence) - 1:
        sol.append(temp)

print(*sol)

    