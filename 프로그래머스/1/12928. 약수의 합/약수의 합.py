def solution(n):
    answer = 0
    
    for i in range(1, int(n**(1/2))+1):
        
        if(n % i == 0 and i * i != n):
            answer += i + (n//i)
        elif(n % i == 0 and i * i == n):
            answer += i
    
    return 1 if n == 1 else answer