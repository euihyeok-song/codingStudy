import sys
from collections import deque

input  = sys.stdin.readline

def bfs(x,y,z):
    
    dq = deque()
    dq.append((x,y,z))
    visited[z][y][x] = 1
    
    # 동서남북상하
    dx = [-1,1,0,0,0,0]
    dy = [0,0,1,-1,0,0]
    dz = [0,0,0,0,1,-1]
    
    while dq:
        x, y, z = dq.popleft()
        
        if graph[z][y][x] == 'E':
            return visited[z][y][x] - 1
        
        for idx in range(6):
            nx = x + dx[idx]
            ny = y + dy[idx]
            nz = z + dz[idx]
            if 0 <= nx < C and 0 <= ny < R and 0 <= nz < L and graph[nz][ny][nx] != '#' and visited[nz][ny][nx] == 0:
                visited[nz][ny][nx] = visited[z][y][x] + 1
                dq.append((nx,ny,nz))
    return -1

while True:
    
    L, R, C = map(int,input().rstrip().split(' '))
    
    if L == 0 and R == 0 and C == 0:
        break
    
    graph = []
    row = []
    visited = [[[0] * C for _ in range(R)] for _ in range(L)]
    cnt = 0

    for _ in range(L):
        graph.append([list(input().rstrip()) for _ in range(R)])
        input()
    
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if graph[i][j][k] == 'S':
                    cnt = bfs(k,j,i)
    
    if cnt >= 0:
        print(f"Escaped in {cnt} minute(s).")
    else:
        print("Trapped!")
    
