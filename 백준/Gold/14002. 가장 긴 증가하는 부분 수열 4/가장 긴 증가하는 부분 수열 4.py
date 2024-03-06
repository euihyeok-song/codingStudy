# 가장 긴 증가하는 부분 수열4

N = int(input())

A = list(map(int,input().split()))

dp = [1]*N

# 가장 긴 증가하는 부분수열을 구하기
for i in range(N):
    for j in range(i):
        if(A[i] > A[j]):
            dp[i] = max(dp[i],dp[j]+1)
            
            
# dp를 쭉 돌면서 가장 길이가 긴 부분 수열의 끝 index를 찾기
max_num = 0
end  = 0
for k in range(N):
    
    if(dp[k] > max_num):
        max_num = dp[k]
        end = k


# 끝 index에 해당하는 A의 원소부터 시작해서 바로 -1씩 되는 지점을 찾아서 stack에 저장
stack = []
stack.append(A[end])
m = end

for index in range(m-1,-1,-1):
    
    if(end == 0):
        break
    
    if(dp[index] == dp[end]-1):
        stack.append(A[index])
        end = index

stack.reverse()
        
print(max_num)
print(*stack)
