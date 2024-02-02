# 후위 표기식2
# 후위 표기식이란 연산자를 연산 대상의 뒤에 쓰는 표기법
# 런타임 에러 발생 -> 사용하는 변수의 갯수를 이용해여함 
# 피연사자가 A~Z인걸 감안해서 판단

import sys

num = int(input())

stack = list(input())

# 미리 ABCDE에 해당하는 숫자를 받은후 각 index를 알파벳의 아스키 코드를 이용해서 계산
number = [int(sys.stdin.readline().rstrip('\n)')) for i in range(num)]

store = []

for val in stack:
    
    if(val >= 'A' and val <= 'Z'):
        index = ord(val) - ord('A')
        store.append(number[index])
    else:
        if(val == '+'):
            result = store.pop() + store.pop()
        elif(val == '-'):
            A = store.pop()
            B = store.pop()
            result = B - A
        elif(val == '*'):
            result = store.pop() * store.pop()
        else:
            A = store.pop()
            B = store.pop()
            result = B / A
        store.append(result)

print(f'{store[-1]:.2f}')
