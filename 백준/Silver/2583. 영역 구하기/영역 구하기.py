import sys
from collections import deque

input = sys.stdin.readline

M, N, K = map(int, input().rstrip().split(' '))

graph = [[0] * N for _ in range(M)]
total_square = []
cnt = 0

def bfs(x,y):
    
    dq = deque()
    dq.append((x,y))
    graph[y][x] = 1
    square = 1
    
    #상하좌우
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    
    while dq:
        x, y = dq.popleft()
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if 0 <= nx < N and 0 <= ny < M and graph[ny][nx] == 0:
                graph[ny][nx] = 1
                dq.append((nx,ny))
                square += 1
    
    return square

for _ in range(K):
    
    left_x , left_y, right_x, right_y = map(int, input().rstrip().split(' '))
    
    # 사각형 해당 영역 먼저 넣기
    for i in range(left_y, right_y):
        for j in range(left_x, right_x):
            graph[i][j] = -1

# bfs 넣기        
for y in range(M):
    for x in range(N):
        if graph[y][x] == 0:
            total_square.append(bfs(x,y))
            cnt += 1

print(cnt)
print(' '.join(map(str,sorted(total_square))))