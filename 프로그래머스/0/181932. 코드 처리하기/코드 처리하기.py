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
    
#   모범답안 => 1을 한개씩 넣어주면서 조건에 맞춰서 짝 -> 홀 -> 짝 모두 결국 [::2]에 맞춰짐  
#   return "".join(code.split("1"))[::2] or "EMPTY"
    return answer if answer else "EMPTY"