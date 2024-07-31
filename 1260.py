# 1260 - DFS & BFS
import sys
from collections import deque
    
# N(정점개수), M(간선개수), V(시작번호))
N, M, V = map(int,input().split(' '))
    
# 방문 여부를 나타내는 visit 배열
visit = [False] * (N+1)
# 경로를 나타내는 배열
node = [[0 for col in range(N+1)] for row in range(N+1)]
    
# 연결된 노드 입력받아서 경로 채워 넣기
for i in range(1,M+1):
    first, second = map(int,sys.stdin.readline().split(' '))
    node[first][second] = node[second][first] = 1


# dfs는 깊이 우선 탐색으로 stack이나 재귀를 많이 사용함 - 재귀 사용해서 구현
def dfs(node,start,visit,path):
    
    visit[start] = True
    path.append(start)
    
    for i in range(1,len(node)):
        if node[start][i] == 1 and visit[i] == False:
            dfs(node,i,visit,path)

# bfs는 너비 우선 탐색으로 deque를 사용함
def bfs(node,start,visit,path):
    
    # 이동할 수 있는 방향(상하좌우)
    
    
    visit[start] = True
    path.append(start)
    
    

# 지나간 dfs history를 담을 배열
d_path = []

# dfs
dfs(node,V,visit,d_path)
print(d_path)

# 지나간 bfs history를 담을 배열
b_path = []
# 공간복잡도를 위해서 배열 재정의
visit = [False] * (N+1)

# bfs
bfs(node,V,visit,b_path)
print(b_path)