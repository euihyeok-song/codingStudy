import math

def solution(n):
    answer = 0
    num = int(math.sqrt(n))
    
    if(num * num == n):
        answer = (num+1) * (num+1)
    else:
        answer = -1
    
        
    return answer