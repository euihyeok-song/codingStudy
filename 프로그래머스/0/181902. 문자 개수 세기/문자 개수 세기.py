def solution(my_string):
    answer = [0] * 52
    
    # A는 65 Z는 90 a는 97 z는 122 => 총 52개
    
    for i in list(my_string):
        
        if(ord(i) >= 65 and ord(i) <= 90):
            answer[ord(i)-65] += 1
        else:
            answer[ord(i)-71] += 1
    
    
    return answer