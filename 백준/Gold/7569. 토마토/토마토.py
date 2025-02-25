import sys
from collections import deque 

input = sys.stdin.readline

M, N, H = map(int,input().rstrip().split(' '))
visited = [[[False] * M for _ in range(N)] for _ in range(H)]
graph = [[list(map(int,input().rstrip().split(' '))) for _ in range(N)] for _ in range(H)]

dq = deque()

# 상하좌우위아래
dx = [0,0,-1,1,0,0]
dy = [1,-1,0,0,0,0]
dz = [0,0,0,0,1,-1]

for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1 and visited[i][j][k] is False:
                dq.append((k,j,i))
                visited[i][j][k] = True
                
def bfs():
    
    while dq:
        x, y, z = dq.popleft()
        for idx in range(6):
            nx = x + dx[idx]
            ny = y + dy[idx]
            nz = z + dz[idx]
            
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and graph[nz][ny][nx] == 0 and visited[nz][ny][nx] is False:
                dq.append((nx,ny,nz))
                graph[nz][ny][nx] = graph[z][y][x] + 1
                visited[nz][ny][nx] = True

bfs()

day = 0

for q in graph: 
    for p in q:
        if 0 in p:
            print(-1)
            exit()
        else:
            day = max(day, max(p))
            
print(day-1)