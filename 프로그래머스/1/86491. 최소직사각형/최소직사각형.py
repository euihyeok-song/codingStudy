def solution(sizes):
    
    max_w = 1
    max_h = 1
    
    for val in sizes:
        
        if(val[0] < val[1]):
            val[0],val[1] = val[1],val[0]
    
        if(max_w < val[0]):
            max_w = val[0]
        
        if(max_h < val[1]):
            max_h = val[1]
    
    return max_w * max_h