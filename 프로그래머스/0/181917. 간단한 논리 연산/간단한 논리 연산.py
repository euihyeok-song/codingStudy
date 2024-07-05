def solution(x1, x2, x3, x4):
    answer = True
    
    first = x1 or x2
    second = x3 or x4
    answer = first and second 
    
    return answer