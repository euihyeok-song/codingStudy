import sys

input = sys.stdin.readline

n = int(input())

curr = 1

stack = []
ans = []

# 수열 입력 받음
for _ in range(n):
    
    seq = int(input())
    
    while curr <= seq:
        stack.append(curr)
        ans.append('+')
        curr += 1
    
    if stack[-1] == seq:
        stack.pop()
        ans.append('-')
    else:
        print("NO")
        exit()

for j in ans:
    print(j)