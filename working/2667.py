# 2667번 - 단지번호 붙이기
from collections import deque

N = int(input())
count = []

graph = [[0 for _ in range(N)] for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]


for i in range(N):
    graph[i] = list(map(int,input()))

def bfs(graph,visited,start):
    
    dq = deque()
    dq.append((start,0))
    cost = 0
    
    # x좌표(상,하,좌,우)
    dx = [0, 0, -1, 1]
    # y좌표(상,하,좌,우)
    dy = [1,-1,0,0]    
    
    while(dq):
        
        curr = dq.popleft()
        
    return cost
        
                
def ooi(x,y):
    return 0 <= x <= N and 0 <= y <= N

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == False:
            count.append(bfs(graph,visited,i))
            
for i in sorted(count):
    print(i)    
    

