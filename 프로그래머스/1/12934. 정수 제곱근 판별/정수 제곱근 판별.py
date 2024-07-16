# import math

def solution(n):
    answer = 0
    
#     num = int(math.sqrt(n))
    
#     if(num * num == n):
#         answer = (num+1) * (num+1)
#     else:
#         answer = -1
    
    # 모범답안
    
    sqrt = n ** (1/2)
    
    if(sqrt % 1 == 0):
        answer = (sqrt+1) ** 2
    else:
        answer = -1
        
    return answer