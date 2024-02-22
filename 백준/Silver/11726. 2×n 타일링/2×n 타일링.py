# 2xN 타일링
# dp를 이용해서 2xN에 대해서 N이 주어졌을때의 1X2와 2X1의 타일로 채울수 있는 방법 수 출력

dp = [0 for i in range(1001)]

dp[1] = 1
dp[2] = 2

for i in range(3,1001):
    
    dp[i] = dp[i-1]+dp[i-2]


# 출력
n = int(input())

print(dp[n] % 10007)