import sys

input = sys.stdin.readline

N, M = map(int,input().rstrip().split(' '))

num = sorted(list(map(int, input().rstrip().split(' '))))
visited = [False] * N
ans = []

def backtracking():
    
    if len(ans) == M:
        print(*ans)
        return
    
    for i in range(N):
        if visited[i] is False:
            visited[i] = True
            ans.append(num[i])
            backtracking()
            ans.pop()
            visited[i] = False

backtracking()