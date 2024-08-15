# 2602법 - 바이러스 (DFS)
# 1번 컴퓨터와 연결되어 있는 모든 컴퓨터를 찾아야 하기 때문에 DFS 사용

def dfs(graph,visit,start):
    
    count = 0
    visit[0][0] = True
    
    for i in range(len(graph)):
        if graph[start][i] == 1 and visit[start][i] == False:
            visit[start][i] = True
            count += 1
            dfs(graph,visit,i)
    
    return count

N = int(input())
M = int(input())

graph = [[0]*(M+1) for _ in range(M)]
visit = [[False]*M for _ in range(M)]
start = 0

for _ in range(M):
    a , b = map(int,input().split(" "))
    graph[a][b] = graph[b][a] = 1
    
print(dfs(graph,visit,start))
