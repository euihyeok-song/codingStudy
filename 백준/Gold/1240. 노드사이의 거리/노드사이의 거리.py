import sys
from collections import deque

def findCost(start,dest):
    
    visited = [False] * (N+1)
    
    dq = deque()
    dq.append((start,0))
    
    visited[start] = True
    
    while(dq):
        v,e = dq.popleft()
        
        if v == dest:
            return e
        
        for idx,val in graph[v]:
            if visited[idx] is False:
                visited[idx] = True
                dq.append((idx, e + val))

input = sys.stdin.readline

N,M = map(int,input().rstrip().split(" "))
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v, cost = map(int, input().rstrip().split(" "))
    
    graph[u].append((v,cost))
    graph[v].append((u,cost))

for _ in range(M):
    
    start, dest = map(int, input().rstrip().split(" "))
    print(findCost(start,dest))