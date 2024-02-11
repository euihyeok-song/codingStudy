# 소수 구하기
# 2부타 자기자신-1 까지 확인 

num = int(input())

prime = list(map(int,input().split(' ')))

count = 0

for i in range(num):
    
    flag = 0
    
    x = prime[i]
    
    if(x == 2):
        count += 1
    
    for j in range(2,x):
        if(x % j == 0):
            flag = 0
            break
        else:
            flag = 1
                
    if(flag == 1):
        count += 1
                
print(count)