# 1,2,3 더하기 3

import sys

T = int(sys.stdin.readline().rstrip('\n'))

dp = [0]*1000001

dp[1]= 1
dp[2]= 2
dp[3]= 4

for i in range(4,1000001):
    dp[i] = (dp[i-1]+dp[i-2]+dp[i-3])%1000000009
    

for _ in range(T):
    
    n = int(sys.stdin.readline().rstrip('\n'))
    
    print(dp[n])