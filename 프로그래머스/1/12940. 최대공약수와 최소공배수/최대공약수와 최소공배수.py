def solution(n, m):
    answer = []
    min = 0
    
    for i in range(1,m+1):
        if(n % i == 0 and m % i == 0 and min < i):
            min = i
            
    answer = [min, min * (n/min) * (m/min)]
            
    
    return answer