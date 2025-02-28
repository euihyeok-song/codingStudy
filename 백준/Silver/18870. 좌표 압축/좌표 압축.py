import sys

input = sys.stdin.readline

N = int(input())
num = list(map(int,input().rstrip().split(' ')))
cnt = []

sort_num = sorted(set(num))

def binary_search(target):
    
    st = 0
    en = len(sort_num)-1
    
    while(st <= en):
        mid = (st+en)//2
        if target > sort_num[mid]:
            st = mid + 1
        elif target < sort_num[mid]:
            en = mid - 1
        else:
            return mid
        
for val in num:
    cnt.append(binary_search(val))

print(*cnt)