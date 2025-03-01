import sys

input = sys.stdin.readline

N, M = map(int,input().rstrip().split(' '))
num = [ int(input()) for _ in range(N)]
min_diff = 2000000000

num.sort()

st, en = 0, 0

while st <= en and en < N:
    
    diff = num[en] - num[st]
    
    if diff >= M:
        min_diff = min(min_diff,diff)
        st += 1
    else:
        en += 1
        
print(min_diff)