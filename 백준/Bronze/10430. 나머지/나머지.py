# 나머지

num = list(input().split(' '))

A = int(num[0])
B = int(num[1])
C = int(num[2])

for i in range(4):
    
    if(i == 0):
        print((A+B)%C)
    elif(i == 1):
        print(((A%C)+(B%C))%C)
    elif(i == 2):
        print((A*B)%C)
    # i == 3
    else:
        print(((A%C)*(B%C))%C)