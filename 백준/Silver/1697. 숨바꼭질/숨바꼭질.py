import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int,input().split(' '))

if N == K:
    print(0)
    exit(0)

visited = [False] * 100001

def bfs():
    
    cnt = 0
    
    dq = deque()
    dq.append((N,cnt))
    visited[N] = True
    
    while dq:
        x, cnt = dq.popleft()
        for nx in [x-1, x+1, x*2]:

            if 0 <= nx <= 100000 and visited[nx] == False:
                if nx == K:
                    print(cnt+1)
                    return
                else:
                    visited[nx] = True
                    dq.append((nx, cnt+1))

bfs()