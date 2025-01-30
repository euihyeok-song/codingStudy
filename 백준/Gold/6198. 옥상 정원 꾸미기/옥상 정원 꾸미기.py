import sys

input = sys.stdin.readline

N = int(input())
cnt = 0

height = [0] * N
stack = []

for i in range(N):
    
    height[i] = int(input())
    
for j in height:
    
    while stack:
        if j < stack[-1]:
            cnt += len(stack)
            break
        else:
            stack.pop()
    stack.append(j)
    
print(cnt)