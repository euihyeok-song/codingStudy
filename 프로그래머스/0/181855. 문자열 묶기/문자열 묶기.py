def solution(strArr):
    answer = 0
    count = [0]* 100000
    
    for i in strArr:
            count[len(i)] += 1
    
    answer = max(count)
            
    return answer