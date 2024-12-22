T = int(input())

for _ in range(T):
    
    R, S = input().split(' ')
    
    answer = ''
    
    for i in range(len(S)):
        
        answer += int(R) * S[i]
    
    print(answer)        
