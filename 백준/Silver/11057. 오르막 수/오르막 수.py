# 오르막 수

N = int(input())

dp = [[1]*10 for _ in range(N+1)]

# dP 조절
for i in range(2,N+1):
    for j in range(10):
        
        if(j == 0):
            dp[i][j] = 1
        else:
            dp[i][j] = (dp[i][j-1]+dp[i-1][j])

total = 0

for k in range(10):
    total += dp[N][k]
    
    
print(total%10007)

        
        
        