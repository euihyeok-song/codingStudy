# 소수 구하기
# 에라토스테네서의 채 이용
import math

M,N = map(int,input().split())

prime = [True for i in range(N+1)]

prime[1] = False

# 에라토스테네서의 채
# math.sqrt(N) == N ** 0.5로 대체 가능
for j in range(2,int(math.sqrt(N))+1):

    if(prime[j] == True):
        
        k=2
        while(j*k <= N):    
            prime[j*k] = False
            k += 1

for idx in range(M,N+1):
    if(prime[idx] == True):
        print(idx)
        
