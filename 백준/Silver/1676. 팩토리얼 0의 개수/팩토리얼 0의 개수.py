# 팩토리얼 0의 개수

num = int(input())

result = 1

count = 0

for i in range(1,num+1):
    
    result *= i
    
j = 10

while(j <= result):
    
    if(result % j == 0):
        count += 1
    else:
        break

    j *= 10
    
print(count)