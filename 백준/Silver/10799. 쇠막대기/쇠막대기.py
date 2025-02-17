import sys

input = sys.stdin.readline

pos = input().rstrip()
stack = []
cnt = 0

pos = pos.replace('()','R')

for val in pos:
    
    if val == 'R':
        cnt += len(stack)
    elif val == '(':
        stack.append(val)
    else:
        stack.pop()
        cnt += 1
    
print(cnt)