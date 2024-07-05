def solution(my_string, indices):
    
    string = list(my_string)
    result = []
    
    for idx,val in enumerate(my_string):
        if(idx not in indices):
            result.append(val)
    answer = ''.join(result)
    
    return answer