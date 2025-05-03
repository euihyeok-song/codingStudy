from collections import deque

def bfs(graph,visited,st_x,st_y):
    
    dq = deque()
    dq.append((st_x,st_y))
    visited[st_y][st_y] = 1
    
    # 상하좌우
    dx, dy = [0,0,-1,1], [1,-1,0,0]
    
    while dq:
        x, y = dq.popleft()
        
        if x == len(graph[0])-1 and y == len(graph)-1:
            return visited[y][x]
            
        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]
            if 0 <= nx < len(graph[0]) and 0 <= ny < len(graph) and visited[ny][nx] == 0 and graph[ny][nx] == 1:
                visited[ny][nx] = visited[y][x] + 1
                dq.append((nx,ny))
    
    return -1
                
def solution(maps):
    
    graph = [ map_val for map_val in maps]
    visited = [[0] * len(graph[0]) for _ in range(len(graph))]
    
    return bfs(graph,visited,0,0)