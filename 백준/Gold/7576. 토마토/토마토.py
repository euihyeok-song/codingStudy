#7575 - 토마토
from collections import deque

N, M = map(int,input().split(' '))
graph = [[0 for _ in range(N)] for _ in range(M)]
dq = deque()

for i in range(M):
    graph[i] = list(map(int,input().split(' ')))
    
def bfs():
    
    # x좌표= 상하좌우
    dx = [0,0,-1,1]
    # y좌표= 상하좌우
    dy = [1,-1,0,0]
    
    while(dq):
        
        x, y = dq.popleft()
        
        for i in range(4):
            curr_x, curr_y = x + dx[i], y + dy[i]
            if 0 <= curr_x < N and 0 <=curr_y < M and graph[curr_y][curr_x] == 0:
                dq.append((curr_x,curr_y))
                graph[curr_y][curr_x] = graph[y][x] + 1
    
for y in range(M):
    for x in range(N):
        if graph[y][x] == 1:
            dq.append((x,y))
            
bfs() 

maxCount = 0

for val in graph:
    if 0 in val:
        print(-1)
        exit(0)
    if maxCount < max(val):
        maxCount = max(val)
        
print(maxCount-1)
    
        
    