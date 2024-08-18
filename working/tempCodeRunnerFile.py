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
    dq.append(start)
    cost = 0
    
    # x좌표(상,하,좌,우)
    dx = [0, 0, -1, 1]
    # y좌표(상,하,좌,우)
    dy = [1,-1,0,0]    
    
    while(dq):
        
        curr = dq.popleft()
        
        for i in range(4):
            curr_x , curr_y = curr[1] + dx[i] , curr[0] + dy[i]
            
            if ooi(curr_x, curr_y) == True and graph[curr_y][curr_x] == 1 and visited[curr_y][curr_x] == False:
                visited[curr_y][curr_x] = True
                dq.append((curr_y,curr_x))
                cost += 1
                
    return cost
        
                
def ooi(x,y):
    return 0 <= x < N and 0 <= y < N

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == False:
            count.append(bfs(graph,visited,(i,j)))
        
print(len(count))
        
for val in sorted(count):
    print(val)

    

