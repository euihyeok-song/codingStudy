def solution(num_list):
    answer = 0
    
    for val in num_list:
        
        while(val != 1):
            # 짝수일 경우
            if(val % 2 == 0):
                val /= 2
            else:
                val = (val-1)/2
            answer += 1
    
    return answer