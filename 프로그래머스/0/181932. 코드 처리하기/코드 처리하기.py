def solution(code):
    answer = ''
    mode = 0
    
    for idx,val in enumerate(code):
        
        if val == "1" and mode == 0:
            mode = 1
        elif val == "1" and mode == 1:
            mode = 0
        elif mode == 0 and idx % 2 == 0:
            answer += val
        elif mode == 1 and idx % 2 == 1:
            answer += val
    
    return answer if answer else "EMPTY"