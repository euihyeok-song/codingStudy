# 카드 구매하기2# 카드 구매하기

# int 값의 최댓값을 구하기 위해 sys.maxint를 사용
import sys

N = int(input())

P = list(map(int,input().split()))

dp = [0 for idx in range(N+1)]

dp[0] = 0

for i in range(1,N+1):
    
    # 현재 과정에서 가장 minx값을 저장해두는 값
    curr = sys.maxsize
    
    for j in range(i):
        
        dp[i] = min(dp[j]+P[i-j-1],curr)
        curr = dp[i]
    
        
print(dp[N])
        
        
        
    
    
    
    