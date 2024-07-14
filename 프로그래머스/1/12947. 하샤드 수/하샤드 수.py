def solution(x):
    answer = True
    digit = list(str(x))
    
    sum = 0
    
    for i in digit:
        sum += int(i)
        
    if x % sum != 0:
         answer = False
    
    
    return answer