# 카드 구매하기

N = int(input())

P = list(map(int,input().split()))

dp = [0 for idx in range(N+1)]

dp[0] = 0

for i in range(1,N+1):
    
    # 현재 과정에서 가장 max값을 저장해두는 값
    curr = 0
    
    for j in range(i):
        
        dp[i] = max(dp[j]+P[i-j-1],curr)
        curr = dp[i]
    
        
print(dp[N])
        
        
        
    
    
    
    