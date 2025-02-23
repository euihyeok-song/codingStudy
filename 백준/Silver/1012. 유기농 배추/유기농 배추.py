import sys
from collections import deque

def bfs(a, b):
    
    dq = deque()
    dq.append((a,b))
    visited[b][a] = True
    
    # 상하좌우
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    
    while dq:
        x, y = dq.popleft()
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            
            if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] == 1 and visited[ny][nx] is False:
                visited[ny][nx] = True
                dq.append((nx,ny))

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    
    M, N, K = map(int,input().rstrip().split(' '))
    
    visited = [[False] * M for _ in range(N)]
    graph = [[0] * M for _ in range(N)]
    cnt = 0
    
    for _ in range(K):
    
        X, Y = map(int,input().rstrip().split(' '))
        graph[Y][X] = 1
        
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and visited[i][j] is False:
                bfs(j,i)
                cnt += 1
                
    print(cnt)