def solution(arr):
    answer = []
    check = []
    
    for idx,val in enumerate(arr):
        if(val == 2):
            check.append(idx)

    if(not check):
        answer = [-1]
    else:
        answer = arr[check[0]:check[-1]+1]
            
    return answer