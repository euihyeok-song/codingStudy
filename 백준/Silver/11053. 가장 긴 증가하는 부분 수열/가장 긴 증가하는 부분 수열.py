# 가장 긴 증가하는 부분 수열
# Longest Incresing Subsequence(LIS)

N = int(input())

A = list(map(int,input().split()))

dp = [1] * N

for i in range(1,N):
    for j in range(i):
        if(A[i] > A[j]):
            dp[i] = max(dp[i], dp[j]+1)

max_num = 0            
for k in range(N):
    
    if(dp[k] > max_num):
        max_num = dp[k]
        
print(max_num)