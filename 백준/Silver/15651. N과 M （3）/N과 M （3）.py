import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split(' '))

visited = [0] * (N+1)
ans = []
cnt = 0

def backtracking():
    
    global cnt
    
    if len(ans) == M:
        print(*ans)
        return
    
    for i in range(1, N+1):
        if visited[i] < M:
            visited[i] += 1
            ans.append(i)
            backtracking()
            visited[i] -= 1
            ans.pop()
            
backtracking()