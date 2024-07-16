def solution(a, b):
    answer = 0
    
    for idx,val in enumerate(a):
        answer += val * b[idx]
    
    return answer