# 시간제한이 1.5초이기 때문에, for문은 1번만 사용하기 ( 2개의 스택, 투포인터는 정렬필요하니 제외)

import sys

input = sys.stdin.readline

N = int(input())

tower = list(map(int, input().split(' ')))
position = [0] * N
stack = []

for i in range(N):
    
    while stack:
        if tower[i] > tower[stack[-1]]:
            stack.pop()
        else:
            position[i] = stack[-1] + 1
            break
    
    stack.append(i)
    
print(*position)