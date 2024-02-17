# Base Conversion

import sys

A ,B = map(int,input().split())
m = int(input())

# 현재 진법으로 구성된 수들
curr = list(map(int,input().split(' ')))

curr.reverse()

result = 0
# step 1 -> curr에 구성된 A진법 수를 10진법 수로 변환
for idx,val in enumerate(curr):
    
    result += val * (A**idx)
    

# 10진법 수를 B진법으로 변환
next = []
while(result > 0):
    
    result, r = result//B, result%B
    next.append(r)
    
for i in range(len(next)):
    
    if(i < len(next)-1):
        print(next.pop(),end= ' ')
    else:
        print(next.pop())