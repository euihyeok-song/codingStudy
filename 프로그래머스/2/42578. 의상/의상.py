def solution(clothes):
    cloth = {}
    answer = 1
    
    for a, b in clothes:
        if b not in cloth:
            cloth[b] = []
        cloth[b].append(b)
    
    for val in cloth:
        answer *= len(cloth[val]) + 1
        
        
    return answer - 1