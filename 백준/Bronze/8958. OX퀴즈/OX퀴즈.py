T = int(input())

for _ in range(T):
    
    sum = 0
    last = 0
    
    result = list(input())

    for i in result:
        
        if i == 'O':
            last += 1
            sum += last
        else:
            last = 0
    
    print(sum)