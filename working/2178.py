# 미로 탐색 - 최소 칸
from collections import deque

# bfs함수
def bfs(graph,visit):
    
    x = y = 0
    dq = deque()
    dq.append((x,y))
    
    visit[0][0] = True
    
    while(dq):
        
        (x,y) = dq.popleft()
        print(x)
        print(y)
        
        # 위로 이동    
        if (y-1) > 0 and graph[y-1][x] == 1 and visit[y-1][x] == False:
            dq.append((x,y-1))
            graph[y-1][x] = graph[y][x] + 1
            
        # 아래로 이동
        if (y+1) > 0 and graph[y+1][x] == 1 and visit[y+1][x] == False:
            dq.append((x,y+1))
            graph[y+1][x] = graph[y][x] + 1
            
        # 왼쪽으로 이동
        if (x-1) > 0 and graph[y][x-1] == 1 and visit[y][x-1] == False:
            dq.append((x-1,y))
            graph[y][x-1] = graph[y][x-1] + 1
            
        # 오른쪽으로 이동
        if (x+1) > 0 and graph[y][x+1] == 1 and visit[y][x+1] == False:

            dq.append((x+1,y))
            graph[y][x+1] = graph[y][x+1] + 1
            
        print(dq)
    
    
    return graph[N-1][M-1]

# N는 행 M은 열
N,M = map(int,input().split(' '))

graph = []
visit = [[False]*M]*N

visit[1][2] = True

print(visit)

for i in range(N):
    a = list(map(int,input()))
    graph.append(a)

print(bfs(graph,visit))

    
