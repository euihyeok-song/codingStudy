# 소인수 분해
# sqrt함수를 사용하기 위해서 math 라이브러리 사용
import math

N = int(input())

# 아래의 방식이 prime = [True] * 10000000보다는 메모리에서 유리함
prime = [True for i in range(10000001)]
prime[0] = False
prime[1] = False

# 에라토테네스의 체를 이용해서 소수구하기
for i in range(2,int(math.sqrt(10000000))+1):
    for j in range(2,i):
        if(i%j ==  0):
           prime[i] = False
           break
       

k = 2
while(N != 1):
    
    if(prime[k] and N%k == 0):
        N //= k
        print(k)
        k = 2
    else:
        k += 1