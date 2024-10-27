# 연결 요소의 개수
import sys
sys.setrecursionlimit(10**6)

def dfs(start):
    
    visit[start] = 1
    
    for i in range(1,len(graph)):
        if graph[start][i] == 1 and visit[i] == 0:
            dfs(i)

N, M = map(int, sys.stdin.readline().split(' '))

graph = [[0]*(N+1) for _ in range(N+1)]
visit = [0 for _ in range(N+1)]
count = 0

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split(' '))
    graph[a][b] = graph[b][a] = 1
    
for j in range(1,N+1):
    if(visit[j] == 0):
        dfs(j)
        count += 1

print(count)