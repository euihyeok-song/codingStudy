def solution(s):
    answer = ''
    result = s.split(' ')

    for val in result:
        for idx,_ in enumerate(val):
            if( idx % 2 == 0):
                answer += val[idx].upper()
            else:
                answer += val[idx].lower()
            
        answer += ' '
        
    return answer[:-1]