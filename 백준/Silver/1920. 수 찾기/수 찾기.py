# 직접 이진 탐색 구현
# import sys

# input = sys.stdin.readline

# N = int(input())
# num = list(map(int,input().rstrip().split(' ')))
# M = int(input())
# is_exist = list(map(int,input().rstrip().split(' ')))

# num.sort()

# def binary_search(target):
    
#     st = 0
#     en = N-1

#     while(st <= en):
#         mid = (st+en)//2
        
#         # mid와 target이 동일할 경우
#         if target == num[mid]:
#             return 1
        
#         # 아닐경우 범주 변경
#         if target > num[mid]:
#             st = mid + 1
#         elif target < num[mid]:
#             en = mid - 1

#     return 0

# # 출력
# for val in is_exist:
#     print(binary_search(val))

# --------------------------------------------------------------------------------------------------------
# 파이썬 라이브러리 사용
import sys
from bisect import bisect_left,bisect_right

input = sys.stdin.readline

N = int(input())
num = list(map(int,input().rstrip().split(' ')))
M = int(input())
is_exist = list(map(int,input().rstrip().split(' ')))

num.sort()

def count_binary_search(arr,val):
    left = bisect_left(num,val)
    right = bisect_right(num,val)
    print(1 if right-left > 0 else 0)
    
for val in is_exist:
    count_binary_search(num,val)