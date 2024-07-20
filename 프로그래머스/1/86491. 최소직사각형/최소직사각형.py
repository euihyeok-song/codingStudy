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
            
    # 모범답안 - sum(sizes,[]) 이런식으로 하면 모든 요소가 flatten한 요소로 들어감
    #        - max(min(size) for size in sizes) : 각 요소 중 작은 값들 중 가장 큰값
    # solution = lambda sizes: max(sum(sizes, [])) * max(min(size) for size in                  sizes)
    
    return max_w * max_h