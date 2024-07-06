def solution(order):
    
    answer = 0
    
    for val in order:
        
        if 'americano' in val:
            answer += 4500
        elif 'cafelatte' in val:
            answer += 5000
        elif 'anything' in val:
            answer += 4500
    
    return answer