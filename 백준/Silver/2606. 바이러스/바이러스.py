# 2602법 - 바이러스 (DFS)
# 1번 컴퓨터와 연결되어 있는 모든 컴퓨터를 찾아야 하기 때문에 DFS 사용

def dfs(start):
    visit[start] = 1    
    
    for i in range(1,len(graph)):
        if graph[start][i] == 1 and visit[i] == 0:
            dfs(i)

N = int(input())
M = int(input())

graph = [[0]*(N+1) for _ in range(N+1)]
visit = [0 for _ in range(N+1)]
start = 1

for _ in range(1,M+1):
    a, b = map(int,input().split(" "))
    graph[a][b] = graph[b][a] = 1
    
dfs(start)    
print(sum(visit)-1)
