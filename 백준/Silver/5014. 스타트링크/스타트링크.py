import sys
from collections import deque

input = sys.stdin.readline

F, S, G, U, D = map(int,input().rstrip().split(' '))

if S == G:
    print(0)
    exit()

# 최대 층수 설정
visited = [0] * (F+1)

def bfs(start,end):
    
    dq = deque()
    dq.append(start)
    visited[start] = 1
    
    while dq:
        x = dq.popleft()
        
        if x == end:
            return visited[x] - 1
        
        for dist in [U,-D]:
            if 1 <= x + dist <= F and visited[x+dist] == 0:
                dq.append(x+dist)
                visited[x+dist] = visited[x] + 1

    return "use the stairs"

print(bfs(S,G))
