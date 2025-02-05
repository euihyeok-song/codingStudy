import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(a, b):
    dq = deque()
    dq.append((a, b))
    graph[a][b] = 0
    count = 1
    
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                dq.append((nx, ny))
                count += 1
                
    return count

picture = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            picture.append(bfs(i, j))

print(len(picture))
print(max(picture) if picture else 0)