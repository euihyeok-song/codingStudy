def solution(intStrs, k, s, l):
    answer = []
    
    for i in range(len(intStrs)):
        change = list(intStrs[i])
        
        num = ''.join(change[s:s+l])
        if(k < int(num)):
            answer.append(int(num))
        
    return answer