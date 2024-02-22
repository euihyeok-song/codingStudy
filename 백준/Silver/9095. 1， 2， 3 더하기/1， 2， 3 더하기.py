# 1,2,3 더하기

import sys

T = int(input())

# n은 11보다 작은 양수
dp = [0 for i in range(11)]

# 1,2,3의 더하기로 구성하기 때문에 1,2,3은 미리 계산후 대입
dp[1] = 1
dp[2] = 2
dp[3] = 4

for j in range(4,11):
    
    dp[j] = dp[j-1] + dp[j-2] + dp[j-3]
    

for k in range(T):
    
    n = int(sys.stdin.readline().rstrip('\n'))
    
    print(dp[n])
