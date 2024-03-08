# 제곱수의 합

# # N의 범위는 1부터 100000까지 이므로, 제곱수는 1부터 316까지만 있으면 됨
# square = [i*i for i in range(317)]

import math

N = int(input())

dp = [idx for idx in range(N+1)]

for i in range(1,N+1):
    for j in range(1,i):
        
        if(j*j > i):
            break
        
        if(dp[i] > dp[i-j*j]+1):
            dp[i] = dp[i-j*j]+1
        
print(dp[N])
        
        
        

