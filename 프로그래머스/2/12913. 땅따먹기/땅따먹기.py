def solution(land):
    
    dp = [[0]*len(land[0]) for _ in range(len(land))]
    
    for i in range(len(land)):
        for j in range(4):
            if i == 0:
                dp[i][j] = land[i][j]
            else:
                dp[i][j] = max(dp[i-1][k] for k in range(4) if k != j) + land[i][j]
        
    return max(dp[-1]) 