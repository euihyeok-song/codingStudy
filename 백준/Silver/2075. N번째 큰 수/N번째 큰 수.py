import heapq
import sys

input = sys.stdin.readline

N = int(input())
heap_nums = []

for _ in range(N):
    nums = list(map(int,input().rstrip().split(" ")))
    
    for num in nums:
        if len(heap_nums) < N:
            heapq.heappush(heap_nums,num)
        else:
            heapq.heappush(heap_nums,num)
            heapq.heappop(heap_nums)

print(heap_nums[0])
