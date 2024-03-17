# 스티커

import sys

T = int(sys.stdin.readline().rstrip('\n'))

for _ in range(T):
    
    N = int(sys.stdin.readline().rstrip('\n'))
    
    cost = []
    cost.append(list(map(int,sys.stdin.readline().rstrip('\n').split())))
    cost.append(list(map(int,sys.stdin.readline().rstrip('\n').split())))
    
    # 선택안함/ 위 선택/ 아래 선택 으로 총 3가지
    dp = [[0]*3 for _ in range(N)]
    
    # 제일 첫번째 가격 저장
    dp[0][1] = cost[0][0]
    dp[0][2] = cost[1][0]
    
    # dp 저장
    for i in range(1,N):
        for j in range(3):
            
            if(j==0):
                # 지금 선택하지 않은 경우
                dp[i][j] = max(dp[i-1][0],dp[i-1][1],dp[i-1][2])
            elif(j==1):
                # 지금 선택이 위인 경우
                dp[i][j] = max(dp[i-1][0],dp[i-1][2]) + cost[0][i]
            elif(j==2):
                # 지금 선택이 아래인 경우
                dp[i][j] = max(dp[i-1][0],dp[i-1][1]) + cost[1][i]
            
    m_num = 0            
    for k in range(3):
        
        if(dp[N-1][k] > m_num):
            m_num = dp[N-1][k]
            
    print(m_num)
