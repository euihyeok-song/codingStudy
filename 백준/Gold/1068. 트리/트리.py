import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = list(map(int,input().rstrip().split(" ")))
M = int(input())
visited = [False] * N
cnt = 0

# 삭제된 노드부터 쭉 타고 들어가면서 연결되어 있는 모든 노드 지우기 (길이 탐색 DFS)
def dfs(root):
    
    graph[root] = -2 # 필요 없는 노드로 변경
    
    for idx in range(N):
        if graph[idx] == root:
            dfs(idx)

dfs(M)

for i in range(N):
    if graph[i] != -2 and i not in graph:
        cnt += 1

print(cnt)