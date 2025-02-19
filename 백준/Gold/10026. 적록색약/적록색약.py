import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]

# BFS 탐색 함수
def bfs(x, y, color, is_special, visited):
    dq = deque([(x, y)])
    visited[y][x] = True
    
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    while dq:
        cx, cy = dq.popleft()
        
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx]:
                if is_special:
                    # 적록색약의 경우 R과 G를 같은 색으로 취급
                    if (color in "RG" and graph[ny][nx] in "RG") or graph[ny][nx] == color:
                        visited[ny][nx] = True
                        dq.append((nx, ny))
                else:
                    if graph[ny][nx] == color:
                        visited[ny][nx] = True
                        dq.append((nx, ny))

# 일반적인 경우
visited_normal = [[False] * N for _ in range(N)]
normal_count = 0

for i in range(N):
    for j in range(N):
        if not visited_normal[i][j]:
            bfs(j, i, graph[i][j], False, visited_normal)
            normal_count += 1

# 적록색약의 경우
visited_special = [[False] * N for _ in range(N)]
special_count = 0

for i in range(N):
    for j in range(N):
        if not visited_special[i][j]:
            bfs(j, i, graph[i][j], True, visited_special)
            special_count += 1

print(normal_count, special_count)
