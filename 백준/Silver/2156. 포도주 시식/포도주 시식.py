# 포도주 시식

import sys

n = int(input())

cost = [0] * n
dp = [0] * n

# n의 범주가 1부터 10000까지 이므로 1과 10000일때도 고려해줘야함
for i in range(n):
    cost[i] = int(sys.stdin.readline().rstrip('\n)'))
    
    if(i == 0):
        dp[i] = cost[i]
    elif(i == 1):
        dp[i] = cost[i-1] + cost[i]
    elif(i == 2):
        dp[i] = max(cost[i-2]+cost[i-1],cost[i-2]+cost[i],cost[i-1]+cost[i])
    
    else:
        # i번째 포도주를 마심
        choice = max(dp[i-3]+cost[i-1]+cost[i],dp[i-2]+cost[i])
        # i번째 포도주를 안마심
        n_choice = dp[i-1]
        
        dp[i] = max(choice, n_choice)
        
print(dp[n-1])