def solution(myStr):
    answer = []
    
    result = myStr.replace('a',' ').replace('b',' ').replace('c',' ')
    
    answer = result.split()
    
    if len(answer) == 0:
        answer.append("EMPTY")
    
    return answer