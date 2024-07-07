def solution(ineq, eq, n, m):
    answer = 0
    
    # eval 함수는 보안상의 이유로 잘 쓰이지는 않는다.
    # answer = int(eval(str(n) + ineq + eq.replace('!','') +str(m)))
    
    if eq == '!' and ineq == '>':
        answer = bool(n - m > 0)
    elif eq == '!' and ineq == '<':
        answer = bool(n - m < 0)
    elif eq == '=' and ineq == '>':
        answer = bool(n - m >= 0)
    else:
        answer = bool(n - m <= 0)       
      
    return int(answer)