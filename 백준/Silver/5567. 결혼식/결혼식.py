# 자신의 친구 + 친구의 친구 
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
# 0과 1 처리
visited = [False,True] + [False] * (n-1)
total = 0

for _ in range(m):    
    a,b = map(int,input().rstrip().split(" "))
    
    graph[a].append(b)
    graph[b].append(a)

def search(start):
    
    cnt = 0
    
    for node in graph[start]:
        if visited[node] is False:
            visited[node] = True
            cnt += 1
    
    return cnt

for node in graph[1]:
    
    if visited[node] is False:
        visited[node] = True
        total += 1

    total += search(node)
    
print(total)