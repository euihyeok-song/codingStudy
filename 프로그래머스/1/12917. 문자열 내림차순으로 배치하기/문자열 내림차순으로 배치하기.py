def solution(s):
    answer = []
    
    result = sorted(list(s),reverse=True)
    
    return ''.join(result)