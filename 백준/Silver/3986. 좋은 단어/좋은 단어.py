import sys

input = sys.stdin.readline

N = int(input())
cnt = 0

for _ in range(N):
    
    word = list(input().rstrip())
    stack = []
    
    # A든 B든 홀수개가 들어오면 Pass
    # if word.count('A') % 2 != 0 or word.count('B') % 2 != 0:
    #    continue
    
    for val in word:
        
        if stack and stack[-1] == val:
            stack.pop()
        else:
            stack.append(val)
            
    if not stack:
        cnt += 1
    
print(cnt)