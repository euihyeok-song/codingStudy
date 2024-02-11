# for문을 이용해서 최소공배수 / 최대공약수 구하기
# 시간 초과 발생 -> 최대공약수를 이용해서 최소공배수 구하기

# 입력받은 str을 int형의 list로 저장
number = list(map(int,input().split(' ')))
              
A = number[0]
B = number[1]

# 최대공약수 구하기
for i in range(min(A,B),0,-1):
    
    if(A % i == 0 and B % i == 0):
        print(i)
        break
       
print(int(i*(A/i)*(B/i)))
        
# 최소공배수 구하기
# for j in range(max(A,B),(A*B)+1):
#     if(j % A == 0 and j % B == 0):
#         print(j)
#         break

