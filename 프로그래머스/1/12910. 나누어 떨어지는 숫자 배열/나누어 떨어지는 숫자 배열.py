def solution(arr, divisor):
    answer = []
    
    for val in arr:
        if val % divisor == 0:
            answer.append(val)
        
    return sorted(answer) if answer else [-1]