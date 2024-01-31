# 오큰수
# 1번째 시도 -> for 문을 두번쓰면 시간초과가 발생 -> for문을 한번만 이용해서 풀도록 짜봄
# stack을 사용해서 풀이

N = int(input())
lis = list(map(int,input().split()))
result = [-1] * N
stack = []
for i in range(N):
    while stack and lis[i]>lis[stack[-1]]: # Step 2부분

        result[stack[-1]]=lis[i] # Step 2 부분

        stack.pop() # Step 3 부분

    stack.append(i) # Step 1 부분
print(*result)


