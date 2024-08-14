# 미로 탐색 - 최소 칸
from collections import deque

# bfs함수
def bfs(graph,visit):
    
    x = y = 0
    dq = deque()
    dq.append((x,y))
    
    # x좌표 방향(상 하 좌 우)
    dx = [0,0,-1,1]
    # y좌표 방향(상 하 좌 우)
    dy = [1,-1,0,0]
    
    visit[0][0] = True
    
    while(dq):
        
        curr = dq.popleft()
        
        for i in range(4):
            result = (curr[0] + dx[i], curr[1] + dy[i])

            if 0 <= result[0] <= M-1 and 0<= result[1] <= N-1 and visit[result[0],result[1]] == False and graph[result[0]][result[1]] == 1:
                graph[result[0]][result[1]] = graph[curr[0]][curr[1]] + 1
                dq.append(result)
            
    
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

    
