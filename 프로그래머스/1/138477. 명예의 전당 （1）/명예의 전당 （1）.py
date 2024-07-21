def solution(k, score):
    answer = []
    result = []
    
    for val in score:
        
        if(len(answer) < k):
            answer.append(val)
        elif(len(answer) >= k and val > min(answer)):
            answer[answer.index(min(answer))] = val
            
        result.append(min(answer))
    
    return result