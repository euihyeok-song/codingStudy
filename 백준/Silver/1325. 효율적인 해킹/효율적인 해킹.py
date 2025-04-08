import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().rstrip().split(" "))
graph = [[] for _ in range(N+1)]
count = [0] * (N+1)
cnt = 0

for _ in range(M):
    
    a,b = map(int, input().rstrip().split(" "))
    
    # A가 B를 신뢰한다 ( B 감염 -> A 감염 ) - 방향성 존재 한방향만
    graph[b].append(a)

def bfs(visited, start):
    
    global cnt
    
    dq = deque()
    dq.append(start)
    visited[start] = 1
    
    while(dq):
        vertex = dq.popleft()
        for node in graph[vertex]:
            if visited[node] == 0:
                dq.append(node)
                visited[node] = 1
                cnt += 1
                
    return cnt

for idx in range(1,N+1):
    
    if graph[idx]:
        visited = [0] * (N+1)
        count[idx] = bfs(visited, idx)
        cnt = 0

result = []

for idx in range(1,N+1):
    if max(count) == count[idx]:
        result.append(idx)

print(*result)