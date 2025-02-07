import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int,input().split(' '))
position = deque(map(int,input().split(' ')))

dq = deque(i+1 for i in range(N))
cnt = 0

while position:
    
    if dq[0] == position[0]:
        dq.popleft()
        position.popleft()
        N -= 1
    elif N  > 2 * dq.index(position[0]):
        dq.append(dq.popleft())
        cnt += 1
    else:
        dq.appendleft(dq.pop())
        cnt += 1
    
print(cnt)

