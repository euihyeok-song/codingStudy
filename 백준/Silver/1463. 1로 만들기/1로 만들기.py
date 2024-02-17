# 1로 만들기 -> 시간제한 0.15초 -> dp를 사용해서 계산횟수를 줄임

X = int(input())

# dp를 만들어서 미리 연산횟수를 만들어 두고, 입력시 횟수 출력
dp = [0 for i in range(1000001)]

# 규칙 1번과 2번에 의해서 2와 3은 연산1번으로 해결됨
dp[2] = 1
dp[3] = 1

# dp를 bottom-up방식을 통해 모든 경우의 연산횟수를 구함
# 최소값을 비교해서 만들도록 선정(ex: 10은 2로 나눠지지만 10->9->3->1이 최솟값)
# 고려사항 = 2와 3 둘다 나눠지는 수 6의배수
for idx in range(4,1000001):
    if(idx % 2 == 0 and idx % 3 != 0):
        dp[idx] = min(dp[idx//2]+1,dp[idx-1]+1)
    elif(idx % 3 == 0 and idx % 2 != 0):
        dp[idx] = min(dp[idx//3]+1,dp[idx-1]+1)
    # 2와 3으로 모두 나눠지는 경우는 3가지중 가장 작은것 선택
    elif(idx % 2 == 0 and idx % 3 == 0):
        dp[idx] = min(dp[idx//2]+1,dp[idx//3]+1,dp[idx-1]+1)
    else:
        dp[idx] = dp[idx-1]+1

print(dp[X])  