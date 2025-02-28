# x + y = k - z 구하기
import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

N = int(input())
num = [int(input()) for _ in range(N)]
sum_xy = []
max_idx = 0

# x + y 구하기
for x in range(N):
    for y in range(x,N):
        sum_xy.append(num[x]+num[y])
        
sum_xy.sort()

def binary_search(target):
    
    st = 0
    en = len(sum_xy)-1
    
    while(st < en):
        mid = (st+en)//2
        if target == sum_xy[mid]:
            return sum_xy[mid]
        elif target < sum_xy[mid]:
            en = mid - 1
        else:
            st = mid + 1
            
for k in num[::-1]:
    for z in num:
        res = binary_search(k-z)
        if res != None:
            max_idx = max(res+z,max_idx)

print(max_idx)