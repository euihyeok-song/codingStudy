import sys
from collections import deque

input = sys.stdin.readline

N ,M = map(int,input().split(' '))
graph = []
visited = [[False] * M for _ in range(N)]

for _ in range(N):
    graph.append(list(map(int,input().rstrip())))
    
def bfs():

    dq = deque()
    
    dq.append((0,0,1))
    visited[0][0] = True
    
    # 상 하 좌 우
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    while dq:
        x, y, cnt= dq.popleft()
        
        # 목적지에 도달하면 종료
        if x == M-1 and y == N-1:
            return cnt
        
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            
            if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] == 1 and visited[ny][nx] == False:
                visited[ny][nx] = True
                dq.append((nx,ny,cnt+1))
            
print(bfs())