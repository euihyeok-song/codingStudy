def solution(n):
    
    dp = [1,2] + [0] * 1998
    
    for idx in range(2,n):
        dp[idx] = dp[idx-1] + dp[idx-2]
                
    return dp[n-1] % 1234567