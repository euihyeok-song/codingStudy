# 2xn 타일링2 
# dp를 이용해서 이전 값들을 저장하고, 점화식의 규칙을 찾아서 해결

dp = [0 for idx in range(1001)]

dp[1] = 1
dp[2] = 3 

for i in range(3,1001):
    
    dp[i] = 2*dp[i-2] + dp[i-1]
    
n = int(input())

print(dp[n] % 10007)
