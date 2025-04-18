def solution(citations):
    
    citations.sort()
    max_num = max(citations)
    answer = 0
    
    for h in range(max_num+1):
        for idx,val in enumerate(citations):
            if val >= h and len(citations)-idx >= h:
                answer = h
    
    return answer