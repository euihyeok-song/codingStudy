def solution(name, yearning, photo):
    answer = []
    dictionary = {name[i]: yearning[i] for i in range(len(name))}
    
    for p in photo:
        score = 0
        for person in p:
            if person in dictionary:
                score += dictionary[person]
        answer.append(score)
        
    return answer
