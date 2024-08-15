# 미로 탐색 - 최소 칸
from collections import deque

# out of index 함수
def ooi(x,y):
    return 0 <= x < M and 0 <= y < N

# bfs함수
def bfs(graph,visit):

    dq = deque()
    dq.append((0,0))
    visit[0][0] = True
    
    # x좌표 방향(상 하 좌 우)
    dx = [0,0,-1,1]
    # y좌표 방향(상 하 좌 우)
    dy = [-1,1,0,0]
    
    while(dq):
        
        curr = dq.popleft()
        
        for i in range(4):
            curr_x = curr[0] + dx[i]
            curr_y = curr[1] + dy[i]
            
            if ooi(curr_x,curr_y) == True:
                if graph[curr_y][curr_x] == 1 and visit[curr_y][curr_x] == False:
                    visit[curr_y][curr_x] = True
                    graph[curr_y][curr_x] = graph[curr[1]][curr[0]] + 1
                    dq.append((curr_x,curr_y))
            
    
    return graph[N-1][M-1]

# N는 행 M은 열
N,M = map(int,input().split(' '))

graph = []
#  이 방식으로 사용하면 [False] * M 크기의 리스트 N개가 하나의 주소를 공유하기 떄문에 문제점 발생
# visit = [[False]*M]*N       
visit = [[False] * M for _ in range(N)]

for i in range(N):
    a = list(map(int,input()))
    graph.append(a)

print(bfs(graph,visit))
    
