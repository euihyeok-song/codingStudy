def solution(rank, attendance):
    answer = 0
    index = rank
    result = []
    
    for idx,val in enumerate(attendance):
        if(val == False):
            rank[idx] = 101
            
    rank = sorted(rank)

    for i in rank:
        if i in index:
            result.append(index.index(i))
        
    
    return result[0]*10000 + result[1]*100 + result[2]