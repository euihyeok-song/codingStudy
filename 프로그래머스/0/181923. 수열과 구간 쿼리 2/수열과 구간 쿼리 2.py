def solution(arr, queries):
    answer = [-1] * len(queries)
    
    for idx, val in enumerate(queries):
        min = 1000000
        for i in range(val[0],val[1]+1):
            if(arr[i] > val[2] and arr[i] < min):
                min = arr[i]
                answer[idx] = min
                
    return answer