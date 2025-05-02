import re

def solution(s):
    
    case, answer = [], []
    sets = re.findall(r'\{([\d,]+)\}', s)
    
    for val in sets:
        case.append(list(map(int,val.split(','))))

    case.sort(key=lambda x:len(x))
    
    for i in case:
        for j in i:
            if j not in answer:
                answer.append(j)
                
    return answer