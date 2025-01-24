import sys

input = sys.stdin.readline

N, K = map(int, input().split(' '))

circle = [i+1 for i in range(N)]
answer = []

idx = 0

while circle:
    
    idx = (idx + K - 1) % len(circle)
    
    answer.append(circle.pop(idx))
    
print("<", end ='')
    
for idx,val in enumerate(answer):
    
    if idx == N-1:
        print(val, end='')
    else:
        print(val, end=', ')
    
print(">")