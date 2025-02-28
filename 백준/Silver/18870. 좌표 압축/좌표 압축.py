import sys
from bisect import bisect_left,bisect_right

N = int(input())
num = list(map(int,input().rstrip().split(' ')))
cnt = []

sort_num = sorted(set(num))

# 해당 값의 가장 왼쪽 값
print(*[bisect_left(sort_num,val) for val in num],sep=' ')