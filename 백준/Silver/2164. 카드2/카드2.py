import sys
from collections import deque;

input = sys.stdin.readline

N = int(input())

dq = deque(i for i in range(N,0,-1))

while True:
    
    if len(dq) == 1:
        break
    
    dq.pop()
    dq.appendleft(dq.pop())

print(*dq)