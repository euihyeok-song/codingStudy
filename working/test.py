# 2667번 - 단지번호 붙이기
from collections import deque

N = int(input())
count = []

graph = [[0 for _ in range(N)] for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]


for i in range(N):
    graph[i] = list(map(int,input()))
    print(graph)