def solution(elements):
    
    result = set()
    element_len, cnt = len(elements), 0
    elements.extend(elements)
    
    for num in range(1,element_len+1):
        for idx in range(element_len):
            result.add(sum(elements[idx:idx+num]))
            
    return len(result)