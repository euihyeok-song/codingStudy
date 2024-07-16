def solution(seoul):
    answer = ''
    index = 0
    
    for idx,val in enumerate(seoul):
        if val == 'Kim':
            index = idx
    
    answer = "김서방은 " + str(index) + "에 있다"
    
    return answer