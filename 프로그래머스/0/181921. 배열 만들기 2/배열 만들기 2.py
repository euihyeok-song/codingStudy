def solution(l, r):
    
    answer = []

    for i in range(l, r+1):        
        result = 0
        num = list(str(i))
        for j in num:
            if j != '0' and int(j) % 5 != 0:
                result = 0
                break
            result = 1
            
        if result == 1:        
            answer.append(i)
                
    
    return answer if answer else [-1]