def solution(strings, n):
    
    answer = []
    result = []
    
    for val in strings:
        answer.append(list(val))
    
    answer.sort(key=lambda x: (x[n],x))
    
    for word in answer:
        result.append(''.join(word))
    
    return result