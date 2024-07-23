def solution(food):
    answer = ''
    result = ''
    
    for idx,val in enumerate(food):
        
        if(idx == 0):
            continue
        
        if(val % 2 != 0):
            food[idx] = val -1
            
    for idx,val in enumerate(food):
        
        if(idx == 0):
            continue
        else:
            answer += str(idx) * (val//2)
    
    result = answer + '0' + answer[::-1]
        
    return result