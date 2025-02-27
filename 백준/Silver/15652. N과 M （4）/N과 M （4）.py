import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split(' '))

visited = [0] * (N+1)
ans = []
result = []

def backtracking(start):
    
    if len(ans) == M:
        print(*ans)
        return
    
    for i in range(start, N+1):
        ans.append(i)
        backtracking(i)
        ans.pop()
            
backtracking(1) 