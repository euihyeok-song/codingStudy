import sys
from bisect import bisect_left,bisect_right

input = sys.stdin.readline

N = int(input())
card = list(map(int,input().rstrip().split(' ')))
M = int(input())
cnt = list(map(int,input().rstrip().split(' ')))

card.sort()

def binary_search(arr,left,right):
    left_idx = bisect_left(arr,left)
    right_idx = bisect_right(arr,right)
    
    return right_idx - left_idx

print(*[binary_search(card,val,val) for val in cnt])
    
    
