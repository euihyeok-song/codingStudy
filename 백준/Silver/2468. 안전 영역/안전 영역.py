import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = []
max_height = 0
max_cnt = 0

for i in range(N):
    row = list(map(int, input().split()))
    graph.append(row)
    max_height = max(max_height, max(row))

def bfs(x, y, k, visited):
    dq = deque([(x, y)])
    visited[y][x] = True
    
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx] and graph[ny][nx] > k:
                visited[ny][nx] = True
                dq.append((nx, ny))

for k in range(max_height):  # 0부터 시작 (비가 내리지 않을 경우 포함)
    cnt = 0
    visited = [[False] * N for _ in range(N)]
    
    for y in range(N):
        for x in range(N):
            if not visited[y][x] and graph[y][x] > k:
                bfs(x, y, k, visited)
                cnt += 1
    
    max_cnt = max(max_cnt, cnt)

print(max_cnt)