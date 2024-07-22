def solution(a, b, n):
    
    answer = 0
    
    while(n >= a):
        result = n // a
        n = (result*b) + (n%a)
        answer += result * b


    
    return answer