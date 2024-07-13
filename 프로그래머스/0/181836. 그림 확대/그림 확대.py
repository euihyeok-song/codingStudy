def solution(picture, k):
    result = []
    answer = []
    
    for val in picture:
        word = ''
        for idx in val:
            word += idx * k
        result.append(word)
        
    for i in result:
        for j in range(k):
            answer.append(i)
    
        
    return answer