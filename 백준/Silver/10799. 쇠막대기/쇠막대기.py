# 쇠막대기

import sys

stick = list(sys.stdin.readline().rstrip('\n'))

stack = []

# 쇠막대기의 갯수
count = 0

# 직전에 들어온 원소를 구분하기 위한 기록
record = 0

for val in stick:
    
    if(val == '('):
        stack.append(val)
        record = 0
    # val == ')'
    else:
        if(record == 0):
            stack.pop()
            count += len(stack)
            record = 1
        else:
            stack.pop()
            count += 1
            
            
print(count)