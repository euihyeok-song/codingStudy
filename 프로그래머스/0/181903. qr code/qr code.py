def solution(q, r, code):
    answer = ''
    
    check = list(code)
    
    for idx,val in enumerate(check):
        if(idx % q == r):
            answer += val
        
    return answer