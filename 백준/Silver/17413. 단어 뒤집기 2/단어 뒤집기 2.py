# 단어 뒤집기 2

import sys

# readline을 통해서 읽어온 문자열을 char형 배열에 저장
sentence = list(sys.stdin.readline())
# 마지막 단어를 알기 위해서 제일 마지막 칸을 " "로 설정 
sentence[-1] = ' '
# print(sentence.__class__)

# tag가 아닌 알파벳이나 숫자를 저장할 stack
stack = []

result = ''

# <>안에 있는지 아닌지 여부
flag = 0

# stack에 저장되어 있는 문자의 총 갯수 판단
count = 0

for i in range(len(sentence)):
    
    # 괄호 내부가 아닐 경우
    if(flag == 0):
        if(sentence[i] == '<'):
            while(count != 0):
                result += stack.pop()
                count -= 1
            result += sentence[i]
            flag = 1
        elif(sentence[i] == ' '):
            while(count != 0):
                result += stack.pop()
                count -= 1
            result += sentence[i]
        else:
            stack.append(sentence[i])
            count += 1
    # 괄호 내부일 경우 (flag = 1)
    else:
        if(sentence[i] == '>'):
            result += sentence[i]
            flag = 0
        else:
            result += sentence[i]
    
print(result)