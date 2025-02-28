import sys

input = sys.stdin.readline

N = int(input())
num = list(map(int,input().rstrip().split(' ')))
M = int(input())
is_exist = list(map(int,input().rstrip().split(' ')))

num.sort()

def binary_search(target):
    
    st = 0
    en = N-1

    while(st <= en):
        mid = (st+en)//2
        
        # mid와 target이 동일할 경우
        if target == num[mid]:
            return 1
        
        # 아닐경우 범주 변경
        if target > num[mid]:
            st = mid + 1
        elif target < num[mid]:
            en = mid - 1

    return 0

# 출력
for val in is_exist:
    print(binary_search(val))