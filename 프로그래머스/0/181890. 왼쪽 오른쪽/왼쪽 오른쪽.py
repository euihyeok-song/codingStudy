def solution(str_list):
    answer = []
    
    for idx,val in enumerate(str_list):
        if(val == "l"):
            answer = str_list[:idx]
            break
        elif(val == "r"):
            answer = str_list[idx+1:]
            break
            
    return answer