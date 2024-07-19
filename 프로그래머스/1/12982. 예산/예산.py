def solution(d, budget):
    answer = 0
    d.sort()
    
    while((budget-d[0]) >= 0):
        
        budget -= d.pop(0)
        answer += 1
        
        if(not d):
            break
        
    return answer