def solution(n, control):
    answer = 0
    
    string = list(control)
    
    for i in range(len(string)):
        
        if(string[i] == 'w'):
            n += 1
        elif(string[i] == 's'):
            n -= 1
        elif(string[i] == 'd'):
            n += 10
        elif(string[i] == 'a'):
            n -= 10
        else:
            continue
            
        answer = n
        
    return answer