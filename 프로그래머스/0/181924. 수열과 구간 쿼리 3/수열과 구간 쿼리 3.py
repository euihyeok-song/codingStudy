def solution(arr, queries):
    answer = []
    tmp = 0
    
    for i in range(len(queries)):
        tmp = arr[queries[i][0]]
        arr[queries[i][0]] = arr[queries[i][1]]
        arr[queries[i][1]] = tmp
    
    answer = arr
    return answer