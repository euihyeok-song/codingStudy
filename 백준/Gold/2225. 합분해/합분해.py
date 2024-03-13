# 합분해

# K는 더할 정수의 갯수/ N은 총 정수 크기
N, K = map(int, input().split())

dp = [[0]*(N+1)]*(K+1)

dp[0][0] = 1
    
# dp 완성하기
for i in range(1,K+1):
    for j in range(N+1):
        
        if(j == 0):
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = dp[i][j-1] + dp[i-1][j]


print(dp[K][N]%1000000000)