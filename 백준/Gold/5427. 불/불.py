import sys
from collections import deque

# 함수 선언
def fire_bfs():
    
    while fire_dq:
        x, y = fire_dq.popleft()
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]

            if 0 <= nx < X and 0 <= ny < Y and graph[ny][nx] == '.' and visited_f[ny][nx] == 0:
                graph[ny][nx] = '*'
                visited_f[ny][nx] = visited_f[y][x] + 1
                fire_dq.append((nx,ny))

def sang_bfs():
    
    while sang_dq:
        x, y = sang_dq.popleft()
        
        if x == 0 or x == X-1 or y == 0 or y == Y-1:
            return visited_s[y][x]
        
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]

            if 0 <= nx < X and 0 <= ny < Y and graph[ny][nx] != '#' and visited_s[ny][nx] == 0:
                if graph[ny][nx] == '*' and visited_f[ny][nx] > visited_s[y][x] + 1:
                    visited_s[ny][nx] = visited_s[y][x] + 1
                    sang_dq.append((nx,ny))
                elif graph[ny][nx] == '.':
                    visited_s[ny][nx] = visited_s[y][x] + 1
                    sang_dq.append((nx,ny))
    
    return "IMPOSSIBLE"

# 입력 시작
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    
    X ,Y = map(int,input().split(' '))
    
    graph = [list(input().rstrip()) for _ in range(Y)]
    visited_f = [[0] * X for _ in range(Y)]
    visited_s = [[0] * X for _ in range(Y)]
    
    fire_dq = deque()
    sang_dq = deque()

    # 상하좌우
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    
    # 불, 상근넣기
    for i in range(Y):
        for j in range(X):
            if graph[i][j] == '@':
                sang_dq.append((j,i))
                visited_s[i][j] = 1
            elif graph[i][j] == '*':
                fire_dq.append((j,i))
                visited_f[i][j] = 1
                
    fire_bfs()
    print(sang_bfs())
    