# RGB거리

import sys

# N은 집의 갯수
N = int(sys.stdin.readline().rstrip('\n'))

cost = []

# 1번집부터 N번 집까지의 빨,초,파 비용을 적어서 저장해둠
for idx in range(N):
    
    cost.append(list(map(int,sys.stdin.readline().rstrip('\n').split())))

for i in range(1,N):
    for j in range(3):
        
        if(j==0):
            cost[i][j] = min(cost[i-1][1]+cost[i][j],cost[i-1][2]+cost[i][j])
        elif(j==1):
            cost[i][j] = min(cost[i-1][0]+cost[i][j],cost[i-1][2]+cost[i][j])
        elif(j==2):
            cost[i][j] = min(cost[i-1][0]+cost[i][j],cost[i-1][1]+cost[i][j])

row = cost[N-1]

print(min(row))