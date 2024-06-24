def solution(arr, queries):
    answer = []
    answer = arr
    
    for s,e in queries:
        for i in range(s,e+1):
            answer[i] += 1
    
    return answer