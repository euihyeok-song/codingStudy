import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split(' '))

graph = [list(input().rstrip()) for _ in range(R)]

# 상하좌우
dx = [0,0,-1,1]
dy = [1,-1,0,0]

dq = deque()
jihun_x, jihun_y = 0, 0

# 불 위치 저장
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'J':
            jihun_x , jihun_y = j, i
        elif graph[i][j] == 'F':
            dq.append((j,i, 'F', 0))

# 지훈 위치 저장
dq.append((jihun_x,jihun_y,'J', 0)) 

def bfs():
    
    cnt = 0
    
    while dq:
        x, y, val, cnt = dq.popleft()
        
        if val == 'J' and (x == 0 or x == C-1 or y == 0 or y == R-1):
            return cnt + 1
                
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            
            if val == 'J':
                if 0 <= nx < C and 0 <= ny < R and graph[ny][nx] == '.':
                    graph[ny][nx] = 'J'
                    dq.append((nx,ny,'J', cnt + 1))
            else:
                if 0 <= nx < C and 0 <= ny < R and graph[ny][nx] == '.':
                    graph[ny][nx] = 'F'
                    dq.append((nx,ny,'F', 0))
    
    return "IMPOSSIBLE"
                    
print(bfs())