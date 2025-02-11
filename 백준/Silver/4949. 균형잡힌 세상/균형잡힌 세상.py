import sys

input = sys.stdin.readline

while True:
    
    sentence = list(input().rstrip())
    
    if sentence[0] == '.':
        break
    
    # 괄호를 저장할 stack
    stack = []
    answer = "yes"
    
    for i in sentence:
        
        if i.isalpha() or i.isspace() or i == '.':
            continue
        else:
            if stack and stack[-1] == '(' and i == ')':
                stack.pop()
            elif stack and stack[-1] == '[' and i == ']':
                stack.pop()
            else:
                stack.append(i)
    
    if stack:
        answer = "no"
            
    print(answer)