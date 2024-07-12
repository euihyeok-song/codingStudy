def solution(arr, k):
    answer = []
    last = -1
    
    for i in arr:
        if(i not in answer):
            answer.append(i)
        
        if(len(answer) == k):
            break
    
    return answer + ([-1] * (k-len(answer)))