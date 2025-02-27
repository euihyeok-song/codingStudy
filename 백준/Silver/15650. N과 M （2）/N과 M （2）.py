import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split(' '))

visited = [False] * (N+1)
ans = []
result = []

def backtracking():
    
    if len(ans) == M:
        if sorted(ans) not in result:
            result.append(sorted(ans))
        return 
        
    for i in range(1,N+1):
        if visited[i] is False:
            visited[i] = True
            ans.append(i)
            backtracking()
            visited[i] = False
            ans.pop()

backtracking()

for val in result:
    print(*val)