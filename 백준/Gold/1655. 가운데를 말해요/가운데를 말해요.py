import sys
import heapq

input = sys.stdin.readline

N = int(input())

left = []
right = []

for _ in range(N):
    num = int(input())
    
    if len(left) == len(right):
        heapq.heappush(left,-num)
    else:
        heapq.heappush(right,num)
    
    if right and (-1 * left[0]) > right[0]:
        first = heapq.heappop(left)
        second = heapq.heappop(right)
        
        heapq.heappush(left,-second)
        heapq.heappush(right,-first)
    
    print(-left[0])