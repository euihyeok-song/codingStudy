def solution(ineq, eq, n, m):
    answer = 0
    
    if eq == '!' and ineq == '>':
        answer = bool(n - m > 0)
    elif eq == '!' and ineq == '<':
        answer = bool(n - m < 0)
    elif eq == '=' and ineq == '>':
        answer = bool(n - m >= 0)
    else:
        answer = bool(n - m <= 0)       
      
    return int(answer)