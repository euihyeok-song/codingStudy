# 이친수

# 자릿수
N = int(input())

# 행(col)은 N자릿수 열(row)는 앞에 오는 수(0,1)
dp = [0 for i in range(91)]

dp[1] = 1
dp[2] = 1

for j in range(3,91):
    
    dp[j] = dp[j-2] + dp[j-1]
    
print(dp[N])