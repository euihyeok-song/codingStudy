import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int,input().rstrip().split(' '))
graph = [list(map(int,input().rstrip())) for _ in range(N)]

# 핵심 포인트는 벽을 부수는 여부를 추가해줘야 한다.
visited = [[[0] * M for _ in range(N)] for _ in range(2)]

def bfs():
    
    dq = deque()
    dq.append((0,0,0))
    visited[0][0][0] = 1
    
    # 상하좌우
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    
    while dq:
        x, y, is_broke = dq.popleft()
        
        if x == M-1 and y == N-1:
            return visited[is_broke][y][x]
        
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if 0 <= nx < M and 0 <= ny < N:
                if graph[ny][nx] == 0 and visited[is_broke][ny][nx] == 0:
                    visited[is_broke][ny][nx] = visited[is_broke][y][x] + 1
                    dq.append((nx,ny,is_broke))
                elif graph[ny][nx] == 1 and is_broke == 0:
                    visited[1][ny][nx] = visited[is_broke][y][x] + 1
                    dq.append((nx,ny,1))
    
    return -1 

print(bfs())