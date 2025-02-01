import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

dq = deque()

for _ in range(N) :
    i = sys.stdin.readline().split()

    if i[0] == 'push' :
        dq.append(int(i[1]))
    
    elif i[0] == 'pop' :
        if not dq :
            print (-1)
        else :
            print(dq[0])
            dq.popleft()
    
    elif i[0] == 'size' :
        print(len(dq))
    
    elif i[0] == 'empty' :
        if len(dq) == 0 :
            print(1)
        else :
            print(0)
    
    elif i[0] == 'front' :
        if not dq:
            print(-1)
        else :
            print(dq[0])
    
    elif i[0] == 'back' :
        if not dq :
            print(-1)
        else :
            print(dq[-1])