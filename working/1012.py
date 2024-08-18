# 1012번 -유기농 배추
from collections import deque

def bfs(graph,visited,start):
    
    y, x = start
    visited[y][x] = True
    dq = deque()
    dq.append((x,y))
    
    # x좌표 상하좌우
    dx = [0, 0, -1, 1]
    # y좌표 상하좌우
    dy = [1, -1, 0 ,0]
    
    while(dq):
        
        x, y = dq.popleft()
        
        for i in range(4):
            curr_x, curr_y = x + dx[i], y + dy[i]
            
            if ooi(curr_x,curr_y) == True and graph[curr_y][curr_x] == 1 and visited[curr_y][curr_x] == False:
                visited[curr_y][curr_x] = True
                dq.append((curr_x,curr_y))
            
            
def ooi(x,y):
    return 0 <= x < N and 0 <= y < M

T = int(input())

for _ in range(T):
    N, M, K = map(int,input().split(' '))
    count = 0

    graph = [[0 for _ in range(N)] for _ in range(M)]
    visited = [[False for _ in range(N)] for _ in range(M)]
    
    for _ in range(K):
        row ,col = map(int,input().split(' '))
        graph[col][row] = 1
        
    for i in range(M):
        for j in range(N):   
            if graph[i][j] == 1 and visited[i][j] == False:
                bfs(graph,visited,(i,j))
                count += 1
    print(count)