import sys

input = sys.stdin.readline

L, C = map(int, input().rstrip().split(' '))

# a,e,i,o,u 중 최소 1개 , 최소 2개의 모음 => a: 97, e: 101, i:105, o:111, u:117
alpha = sorted(list(input().rstrip().split(' ')))
cons = ['a','e','i','o','u']
ans = []

# 자음 포함 여부 (1이면 자음 포함)
flag = -1

def backtracking(start):
    
    global flag
    
    if len(ans) == L and -1 < flag < L-2:
        print(''.join(ans))
        return
    
    for i in range(start,C):
        
        if alpha[i] in cons:
            flag += 1
        
        ans.append(alpha[i])
        backtracking(i+1)
        if ans.pop() in cons:
            flag -= 1
        
backtracking(0)